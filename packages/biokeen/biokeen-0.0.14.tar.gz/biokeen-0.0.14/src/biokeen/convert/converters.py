# -*- coding: utf-8 -*-

"""Conversion base classes."""

from abc import ABC, abstractmethod
from typing import Dict, Tuple

from pybel.constants import (
    ACTIVITY, ASSOCIATION, CORRELATIVE_RELATIONS, DECREASES, DIRECTLY_DECREASES, DIRECTLY_INCREASES, EQUIVALENT_TO,
    HAS_COMPONENT, INCREASES, IS_A, MODIFIER, OBJECT, PART_OF, REGULATES, RELATION,
)
from pybel.dsl import (
    Abundance, BaseAbundance, BaseEntity, BiologicalProcess, ComplexAbundance, MicroRna,
    NamedComplexAbundance, Pathology, Protein, Rna,
)


class Converter(ABC):
    """A condition and converter for a BEL edge."""

    @staticmethod
    @abstractmethod
    def predicate(u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> bool:
        """Test a BEL edge."""

    @staticmethod
    @abstractmethod
    def convert(u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> Tuple[str, str, str]:
        """Convert a BEL edge."""


class SimpleConverter(Converter):
    """A class for converting the source and target that have simple names."""

    @classmethod
    def convert(cls, u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> Tuple[str, str, str]:
        """Convert a BEL edge."""
        return (
            f'{u.namespace}:{u.identifier or u.name}',
            edge_data[RELATION],
            f'{v.namespace}:{v.identifier or v.name}',
        )


class TypedConverter(Converter):
    """A class for converting the source and target but replaces the relation."""

    target_relation = None

    @classmethod
    def convert(cls, u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> Tuple[str, str, str]:
        """Convert a BEL edge."""
        return (
            f'{u.namespace}:{u.identifier or u.name}',
            cls.target_relation,
            f'{v.namespace}:{v.identifier or v.name}',
        )


class SimplePredicate(Converter):
    """Converts BEL statements based on a given relation."""

    relation = ...

    @classmethod
    def predicate(cls, u, v, key, edge_data) -> bool:
        """Test a BEL edge has a given relation."""
        return edge_data[RELATION] == cls.relation


class SimpleTypedPredicate(SimplePredicate):
    """Finds BEL statements like ``A(X) B C(Y)`` where relation B and types A and C are defined in the class."""

    subject_type = ...
    object_type = ...

    @classmethod
    def predicate(cls, u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> bool:
        """Test a BEL edge."""
        return super().predicate(u, v, key, edge_data) and (
            isinstance(u, cls.subject_type) and
            isinstance(v, cls.object_type)
        )


class _PartOfConverter(SimpleTypedPredicate, TypedConverter):
    relation = PART_OF
    target_relation = 'partOf'


class PartOfNamedComplexConverter(_PartOfConverter):
    """Converts BEL statements like ``p(X) partOf complex(Y)``."""

    subject_type = Protein
    object_type = NamedComplexAbundance


class SubprocessPartOfBiologicalProcess(_PartOfConverter):
    """Converts BEL statements like ``bp(X) partOf bp(Y)``."""

    subject_type = BiologicalProcess
    object_type = BiologicalProcess


class ProteinPartOfBiologicalProcess(_PartOfConverter):
    """Converts BEL statements like ``p(X) partOf bp(Y)``."""

    subject_type = Protein
    object_type = BiologicalProcess


class NamedComplexHasComponentConverter(SimpleTypedPredicate):
    """Converts BEL statements like ``complex(X) hasComponent p(Y)``."""

    subject_type = NamedComplexAbundance
    relation = HAS_COMPONENT
    object_type = Protein
    target_relation = 'partOf'

    @classmethod
    def convert(cls, u: BaseEntity, v: BaseEntity, key: str, data: Dict) -> Tuple[str, str, str]:
        """Convert a BEL edge."""
        return (
            f'{v.namespace}:{v.identifier or v.name}',
            cls.target_relation,
            f'{u.namespace}:{u.identifier or u.name}',
        )


class ListComplexHasComponentConverter(SimpleTypedPredicate):
    """Converts BEL statements like ``complex(p(X), p(Y), ...) hasComponent p(X)``."""

    subject_type = ComplexAbundance
    relation = HAS_COMPONENT
    object_type = Protein
    target_relation = 'partOf'

    @classmethod
    def convert(cls, u: ComplexAbundance, v: BaseAbundance, key: str, data: Dict) -> Tuple[str, str, str]:
        """Convert a BEL edge."""
        return (
            f'{v.namespace}:{v.identifier or v.name}',
            cls.target_relation,
            str(u),
        )


'''
class TranslationConverter(TypedConverter):
    relation = TRANSLATED_TO
    target_relation = 'ribosomallyTranslatesTo'


class TranscriptionConverter(TypedConverter):
    relation = TRANSCRIBED_TO
    target_relation = 'ribosomallyTranslatesTo'
'''


class IsAConverter(SimplePredicate, SimpleConverter):
    """Converts BEL statements like ``X isA Y``."""

    relation = IS_A
    target_relation = 'isA'


class EquivalenceConverter(SimplePredicate, SimpleConverter):
    """Converts BEL statements like ``X eq Y``."""

    relation = EQUIVALENT_TO
    target_relation = 'equivalentTo'


class CorrelationConverter(SimpleConverter):
    """Converts BEL statements like ``A(B) pos|neg|noCorrelation C(D)``."""

    @staticmethod
    def predicate(u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> bool:
        """Test a BEL edge."""
        return edge_data[RELATION] in CORRELATIVE_RELATIONS


class AssociationConverter(Converter):
    """Converts BEL statements like ``a(X) -- path(Y)``."""

    @staticmethod
    def predicate(u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> bool:
        """Test a BEL edge."""
        return edge_data[RELATION] == ASSOCIATION

    @staticmethod
    def convert(u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> Tuple[str, str, str]:
        """Convert a BEL edge."""
        return (
            f'{u.namespace}:{u.identifier or u.name}',
            edge_data.get('association_type', ASSOCIATION),  # allow more specific association to be defined
            f'{v.namespace}:{v.identifier or v.name}',
        )


class DrugEffectConverter(SimpleConverter, SimpleTypedPredicate):
    """Converts BEL statements like ``a(X) ? path(Y)``."""

    subject_type = Abundance
    relation = ...
    object_type = Pathology


class DrugIndicationConverter(DrugEffectConverter):
    """Converts BEL statements like ``a(X) -| path(Y)``."""

    relation = DECREASES


class DrugSideEffectConverter(DrugEffectConverter):
    """Converts BEL statements like ``a(X) -> path(Y)``."""

    relation = INCREASES


class RegulatesAmountConverter(TypedConverter):
    """Converts BEL statements like ``A(B) reg C(D)``."""

    relation = REGULATES
    target_relation = 'regulatesAmountOf'

    @classmethod
    def predicate(cls, u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> bool:
        """Test a BEL edge."""
        object_modifier = edge_data.get(OBJECT)
        return edge_data[RELATION] == cls.relation and (not object_modifier or not object_modifier.get(MODIFIER))


class IncreasesAmountConverter(RegulatesAmountConverter):
    """Converts BEL statements like ``A(B) -> C(D)``."""

    relation = INCREASES
    target_relation = 'increasesAmountOf'


class DecreasesAmountConverter(RegulatesAmountConverter):
    """Converts BEL statements like ``A(B) -| C(D)``."""

    relation = DECREASES
    target_relation = 'decreasesAmountOf'


class RegulatesActivityConverter(TypedConverter):
    """Converts BEL statements like ``A(B) reg act(C(D) [, ma(E)])``."""

    relation = REGULATES
    target_relation = 'activityDirectlyRegulatesActivityOf'

    @classmethod
    def predicate(cls, u: BaseEntity, v: BaseEntity, key: str, edge_data: Dict) -> bool:
        """Test a BEL edge."""
        object_modifier = edge_data.get(OBJECT)
        return edge_data[RELATION] == cls.relation and object_modifier and object_modifier.get(MODIFIER) == ACTIVITY


class IncreasesActivityConverter(RegulatesActivityConverter):
    """Converts BEL statements like ``A(B) -> act(C(D) [, ma(E)])``."""

    relation = INCREASES
    target_relation = 'activityDirectlyPositivelyRegulatesActivityOf'


class DecreasesActivityConverter(RegulatesActivityConverter):
    """Converts BEL statements like ``A(B) -| act(C(D) [, ma(E)])``."""

    relation = DECREASES
    target_relation = 'activityDirectlyNegativelyRegulatesActivityOf'


class MiRNARegulatesExpressionConverter(TypedConverter, SimpleTypedPredicate):
    """Converts BEL statements like ``m(X) reg r(Y)``."""

    subject_type = MicroRna
    relation = REGULATES
    object_type = Rna
    target_relation = 'regulatesExpressionOf'


class MiRNAIncreasesExpressionConverter(MiRNARegulatesExpressionConverter):
    """Converts BEL statements like ``m(X) -> r(Y)``."""

    relation = INCREASES
    target_relation = 'increasesExpressionOf'


class MiRNADirectlyIncreasesExpressionConverter(MiRNARegulatesExpressionConverter):
    """Converts BEL statements like ``m(X) => r(Y)``."""

    relation = DIRECTLY_INCREASES
    target_relation = 'increasesExpressionOf'


class MiRNADecreasesExpressionConverter(MiRNARegulatesExpressionConverter):
    """Converts BEL statements like ``m(X) -| r(Y)``."""

    relation = DECREASES
    target_relation = 'repressesExpressionOf'


class MiRNADirectlyDecreasesExpressionConverter(MiRNARegulatesExpressionConverter):
    """Converts BEL statements like ``m(X) =| r(Y)``."""

    relation = DIRECTLY_DECREASES
    target_relation = 'repressesExpressionOf'
