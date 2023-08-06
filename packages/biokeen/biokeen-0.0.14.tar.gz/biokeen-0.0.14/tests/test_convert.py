# -*- coding: utf-8 -*-

"""Tests for the conversion procedure."""

import unittest
from typing import Tuple, Type

from biokeen.convert import get_triple
from biokeen.convert.converters import (
    AssociationConverter, Converter, CorrelationConverter, DecreasesAmountConverter, DrugIndicationConverter,
    DrugSideEffectConverter, EquivalenceConverter, IncreasesAmountConverter, IsAConverter,
    MiRNADecreasesExpressionConverter, NamedComplexHasComponentConverter,
    PartOfNamedComplexConverter, RegulatesActivityConverter, RegulatesAmountConverter, SubprocessPartOfBiologicalProcess
)
from pybel import BELGraph
from pybel.constants import (
    ASSOCIATION, DECREASES, EQUIVALENT_TO, HAS_COMPONENT, INCREASES, IS_A, NEGATIVE_CORRELATION, OBJECT, PART_OF,
    POSITIVE_CORRELATION, REGULATES, RELATION,
)
from pybel.dsl import (
    Abundance, BaseEntity, BiologicalProcess, MicroRna, NamedComplexAbundance, Pathology, Protein,
    Rna, activity,
)
from pybel.testing.utils import n
from pybel.typing import EdgeData


def _rel(x):
    return {RELATION: x}


def _rela(x, y=None):
    return {RELATION: x, OBJECT: activity(y)}


def _assoc(y):
    return {RELATION: ASSOCIATION, 'association_type': y}


a1 = Abundance('CHEBI', '1')
p1 = Protein('HGNC', '1')
pf1 = Protein('INTERPRO', '1')
d1 = Pathology('MESH', '1')
b1 = BiologicalProcess('GO', '1')
b2 = BiologicalProcess('GO', '2')
m1 = MicroRna('MIRBASE', '1')
r1 = Rna('HGNC', '1')
r2 = Rna('HGNC', '2')
nca1 = NamedComplexAbundance('FPLX', '1')

converters_true_list = [
    (NamedComplexHasComponentConverter, nca1, p1, _rel(HAS_COMPONENT), ('HGNC:1', 'partOf', 'FPLX:1')),
    (PartOfNamedComplexConverter, p1, nca1, _rel(PART_OF), ('HGNC:1', 'partOf', 'FPLX:1')),
    (SubprocessPartOfBiologicalProcess, b1, b2, _rel(PART_OF), ('GO:1', 'partOf', 'GO:2')),
    (AssociationConverter, r1, r2, _rel(ASSOCIATION), ('HGNC:1', 'association', 'HGNC:2')),
    (AssociationConverter, r1, r2, _assoc('similarity'), ('HGNC:1', 'similarity', 'HGNC:2')),
    (CorrelationConverter, r1, r2, _rel(POSITIVE_CORRELATION), ('HGNC:1', 'positiveCorrelation', 'HGNC:2')),
    (IsAConverter, p1, pf1, _rel(IS_A), ('HGNC:1', 'isA', 'INTERPRO:1')),
    # Found in ADEPTUS
    (CorrelationConverter, d1, r1, _rel(POSITIVE_CORRELATION), ('MESH:1', 'positiveCorrelation', 'HGNC:1')),
    (CorrelationConverter, d1, r1, _rel(NEGATIVE_CORRELATION), ('MESH:1', 'negativeCorrelation', 'HGNC:1')),
    # Found in LINCS (not integrated yet)
    (RegulatesAmountConverter, a1, r1, _rel(REGULATES), ('CHEBI:1', 'regulatesAmountOf', 'HGNC:1')),
    (IncreasesAmountConverter, a1, r1, _rel(INCREASES), ('CHEBI:1', 'increasesAmountOf', 'HGNC:1')),
    (DecreasesAmountConverter, a1, r1, _rel(DECREASES), ('CHEBI:1', 'decreasesAmountOf', 'HGNC:1')),
    # Found in SIDER
    (DrugSideEffectConverter, a1, d1, _rel(INCREASES), ('CHEBI:1', 'increases', 'MESH:1')),
    (DrugIndicationConverter, a1, d1, _rel(DECREASES), ('CHEBI:1', 'decreases', 'MESH:1')),
    # Found in miRTarBase
    (MiRNADecreasesExpressionConverter, m1, r1, _rel(DECREASES), ('MIRBASE:1', 'repressesExpressionOf', 'HGNC:1')),
    # Found in DrugBank
    (RegulatesActivityConverter, a1, p1, _rela(REGULATES), ('CHEBI:1', 'activityDirectlyRegulatesActivityOf',
                                                            'HGNC:1')),
    # Found in ComPath
    (EquivalenceConverter, b1, b2, _rel(EQUIVALENT_TO), ('GO:1', 'equivalentTo', 'GO:2')),
    (SubprocessPartOfBiologicalProcess, b1, b2, _rel(PART_OF), ('GO:1', 'partOf', 'GO:2')),
    # Found in HSDN
]

converters_false_list = [
    (NamedComplexHasComponentConverter, nca1, p1, _rel(PART_OF)),
    (PartOfNamedComplexConverter, nca1, p1, _rel(HAS_COMPONENT)),
]


class TestConverters(unittest.TestCase):
    """Tests for the converter classes."""

    def help_test_convert(self,
                          converter: Type[Converter],
                          u: BaseEntity,
                          v: BaseEntity,
                          edge_data: EdgeData,
                          triple: Tuple[str, str, str],
                          ) -> None:
        """Test a converter class."""
        self.assertTrue(issubclass(converter, Converter), msg=f'Not a Converter: {converter.__name__}')
        key = n()
        self.assertTrue(
            converter.predicate(u, v, key, edge_data),
            msg=f'Predicate failed: {converter.__name__}',
        )
        self.assertEqual(
            triple,
            converter.convert(u, v, key, edge_data),
            msg=f'Conversion failed: {converter.__name__}',
        )
        graph = BELGraph()
        graph.add_edge(u, v, key=key, **edge_data)
        self.assertEqual(
            triple,
            get_triple(graph, u, v, key),
            msg=f'get_triple failed: {converter.__name__}',
        )

    def test_converters_true(self):
        """Test passing converters."""
        for converter, u, v, edge_data, triple in converters_true_list:
            with self.subTest(msg=f'Converter: {converter.__qualname__}'):
                self.help_test_convert(converter, u, v, edge_data, triple)

    def test_converters_false(self):
        """Test falsification of converters."""
        for converter, u, v, edge_data in converters_false_list:
            with self.subTest():
                self.assertFalse(converter.predicate(u, v, n(), edge_data))
