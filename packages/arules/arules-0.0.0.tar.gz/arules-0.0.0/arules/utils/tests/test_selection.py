import unittest
import pandas as pd
from ...association_rules import create_association_rules
from ..selection import _rules_by_var

class SelectionTest(unittest.TestCase):
    def setUp(self):
        self.cols = ['rule print', 'ant_supp', 'con_supp', 'rule_supp', 'confidence', 'lift', '# of records']
        self.sample_df = pd.DataFrame.from_dict({'1': {'A': 'a1', 'B': 'b1', 'C': 'c1', 'D': 'd1'},
                                                 '2': {'A': 'a1', 'B': 'b2', 'C': 'c1', 'D': 'd2'},
                                                 '3': {'A': 'a2', 'B': 'b1', 'C': 'c1', 'D': 'd2'},
                                                 '4': {'A': 'a3', 'B': 'b3', 'C': 'c2', 'D': 'd2'},
                                                 '5': {'A': 'a1', 'B': 'b1', 'C': 'c2', 'D': 'd3'},
                                                 '6': {'A': 'a3', 'B': 'b2', 'C': 'c3', 'D': 'd2'},
                                                 '7': {'A': 'a2', 'B': 'b1', 'C': 'c1', 'D': 'd1'},
                                                 '8': {'A': 'a1', 'B': 'b3', 'C': 'c1', 'D': 'd2'},
                                                 '9': {'A': 'a3', 'B': 'b1', 'C': 'c2', 'D': 'd3'},
                                                 '10': {'A': 'a1', 'B': 'b1', 'C': 'c3', 'D': 'd1'}}, orient='index')
        self.association_rules_by_var = pd.DataFrame.from_records(
            [{'rule print': "A=a1 ==> B=b1", 'ant_supp': 5, 'con_supp': 6,
              'rule_supp': 3, 'confidence': 3 / 5, 'lift': (3 / 5) / (6 / 10),
              '# of all records': 10},
             {'rule print': "A=a1 ==> B=b2", 'ant_supp': 5, 'con_supp': 2,
              'rule_supp': 1, 'confidence': 1 / 5,
              'lift': (1 / 5) / (2 / 10),
              '# of all records': 10},
             {'rule print': "A=a1 ==> B=b3", 'ant_supp': 5, 'con_supp': 2,
              'rule_supp': 1, 'confidence': 1 / 5,
              'lift': (1 / 5) / (2 / 10),
              '# of all records': 10},
             {'rule print': "A=a2 ==> B=b1", 'ant_supp': 2, 'con_supp': 6,
              'rule_supp': 2, 'confidence': 1,
              'lift': 1 / (6 / 10),
              '# of all records': 10},
             {'rule print': "A=a3 ==> B=b1", 'ant_supp': 3, 'con_supp': 6,
              'rule_supp': 1, 'confidence': 1 / 3,
              'lift': (1 / 3) / (6 / 10),
              '# of all records': 10},
             {'rule print': "A=a3 ==> B=b2", 'ant_supp': 3, 'con_supp': 2,
              'rule_supp': 1, 'confidence': 1 / 3,
              'lift': (1 / 3) / (2 / 10),
              '# of all records': 10},
             {'rule print': "A=a3 ==> B=b3", 'ant_supp': 3, 'con_supp': 2,
              'rule_supp': 1, 'confidence': 1 / 3,
              'lift': (1 / 3) / (2 / 10),
              '# of all records': 10}], columns=self.cols)

    def test_rules_by_var(self):
        ass_rules, _ = create_association_rules(self.sample_df, ['A', 'B'])
        rules_by_var = _rules_by_var(ass_rules,frozenset(['A']))
        self.assertEqual(set(self.association_rules_by_var['rule print']), set(rules_by_var['rule print']),
                         "Dropping rule duplicate was not done properly")