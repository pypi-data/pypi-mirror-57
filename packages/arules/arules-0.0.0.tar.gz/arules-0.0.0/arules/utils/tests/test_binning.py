import unittest
from ..binning import _set_rounding_parameter, _create_labels


class BinningTest(unittest.TestCase):
    def test_set_rounding_parameter(self):
        zero_test = [0,1,2,3,4,5]
        for i in range(5):
            i_test = [element/(10**i) for element in zero_test]
            i_param = _set_rounding_parameter(i_test)
            self.assertEqual(i_param, i, 'Round parameter was calculated properly for ' + str(i) + ' list')

    def test_create_labels(self):
        bins_list = [0,1,2,3,4,5]
        labels = _create_labels(bins_list,0)
        self.assertEqual(labels,['[0 - 1]','(1 - 2]','(2 - 3]','(3 - 4]','(4 - 5]'],"Labels were not created properly")

