# flake8: noqa
from unittest import TestCase

from pyevolve import G1DBinaryString
from pyevolve import G1DList
from pyevolve import G2DBinaryString
from pyevolve import G2DList
from pyevolve.GenomeBase import G1DBase
from pyevolve.GenomeBase import GTreeBase
from pyevolve.GTree import GTree
from pyevolve.GTree import GTreeNode
from pyevolve.GTree import GTreeNodeBase
from pyevolve.GTree import GTreeNodeGP


class G1DBinaryStringTestCase(TestCase):

    # def setUp(self):
    #     self._stats = Statistics.Statistics()

    def test_create1DBinary_default(self):
        _genome = G1DBinaryString.G1DBinaryString()
        self.assertTrue(hasattr(_genome, 'genomeList'))
        self.assertTrue(hasattr(_genome, 'genomeSize'))
        self.assertIsInstance(_genome.genomeSize, int)
        self.assertTrue(hasattr(_genome, 'initializator'))
        self.assertTrue(hasattr(_genome, 'mutator'))
        self.assertTrue(hasattr(_genome, 'crossover'))

    def test_create1DBinary_len(self):
        _genome = G1DBinaryString.G1DBinaryString(length=5)
        self.assertTrue(hasattr(_genome, 'genomeList'))
        self.assertEqual(_genome.genomeSize, 5)
        self.assertTrue(hasattr(_genome, 'initializator'))
        self.assertTrue(hasattr(_genome, 'mutator'))
        self.assertTrue(hasattr(_genome, 'crossover'))

    def test_1DBinarySetitem(self):
        _genome = G1DBinaryString.G1DBinaryString(length=5)
        _genome.append(0)
        _genome.append(1)
        _genome.append(1)
        self.assertEqual(_genome[0], 0)
        with self.assertRaises(ValueError):
            _genome[0] = 2
        with self.assertRaises(ValueError):
            _genome[0:2] = [0,1,2]

    def test_getBinary(self):
        _genome = G1DBinaryString.G1DBinaryString()
        self.assertIsInstance(_genome.getBinary(), str)

    def test_getDecimal(self):
        _genome = G1DBinaryString.G1DBinaryString(length=3)
        _genome.append(0)
        _genome.append(1)
        _genome.append(1)
        self.assertEqual(_genome.getDecimal(), 3)

    def test_append(self):
        _genome = G1DBinaryString.G1DBinaryString(length=3)
        _genome.append(0)
        _genome.append(1)
        self.assertEqual(_genome[0], 0)
        with self.assertRaises(ValueError):
            _genome.append(2)

    def test_repr(self):
        _genome = G1DBinaryString.G1DBinaryString()
        self.assertIsInstance(repr(_genome), str)