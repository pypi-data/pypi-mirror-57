import unittest
from arules import association_rules as ar
import numpy as np
import pandas as pd
from arules.utils import five_quantile_based_bins


class AssociationRulesTest(unittest.TestCase):
    def setUp(self):
        self.set_of_4_formats = set([(1,1),(1,2),(2,1),(2,2),(1,3),(3,1)])
        self.set_of_ant_1_formats = set([(1,1),(1,2),(1,3)])
        self.set_of_con_1_formats = set([(1,1),(2,1),(3,1)])
        self.list_of_cols = ['A','B','C','D']
        self.list_of_2_1_rules = [{'ant': ['A','B'], 'con':['C']}, {'ant': ['A','D'], 'con':['C']},
                                  {'ant': ['B','D'], 'con':['C']}, {'ant': ['A','B'], 'con':['D']},
                                  {'ant': ['A','C'], 'con':['D']}, {'ant': ['B','C'], 'con':['D']},
                                  {'ant': ['B','C'], 'con':['A']}, {'ant': ['B','D'], 'con':['A']},
                                  {'ant': ['C','D'], 'con':['A']}, {'ant': ['A','C'], 'con':['B']},
                                  {'ant': ['A','D'], 'con':['B']}, {'ant': ['C','D'], 'con':['B']}]
        self.sample_df = pd.DataFrame.from_dict({'1': {'A': 'a1','B':'b1','C':'c1','D':'d1'},
                                                 '2': {'A': 'a1','B':'b2','C':'c1','D':'d2'},
                                                 '3': {'A': 'a2','B':'b1','C':'c1','D':'d2'},
                                                 '4': {'A': 'a3','B':'b3','C':'c2','D':'d2'},
                                                 '5': {'A': 'a1','B':'b1','C':'c2','D':'d3'},
                                                 '6': {'A': 'a3','B':'b2','C':'c3','D':'d2'},
                                                 '7': {'A': 'a2','B':'b1','C':'c1','D':'d1'},
                                                 '8': {'A': 'a1','B':'b3','C':'c1','D':'d2'},
                                                 '9': {'A': 'a3','B':'b1','C':'c2','D':'d3'},
                                                 '10': {'A': 'a1','B':'b1','C':'c3','D':'d1'}},orient='index')
        self.set_of_sups = set([frozenset(['A']),frozenset(['B']),frozenset(['C']),frozenset(['B','A']),
                                frozenset(['C','A']),frozenset(['B','C']),frozenset(['C','A','B'])])
        self.sup_A = pd.Series({'a1':5,'a2':2,'a3':3})
        self.variable_rule_list = [{'ant': ['B'], 'con':['D']}, {'ant': ['A', 'B'], 'con':['C']}]
        self.rule_list = ["B=b1 ==> D=d1",  "B=b1 ==> D=d2", "B=b1 ==> D=d3", "B=b2 ==> D=d2", "B=b3 ==> D=d2",
                          "A=a1, B=b1 ==> C=c1", "A=a1, B=b2 ==> C=c1", "A=a2, B=b1 ==> C=c1", "A=a3, B=b3 ==> C=c2",
                          "A=a1, B=b1 ==> C=c2", "A=a3, B=b2 ==> C=c3", "A=a1, B=b3 ==> C=c1", "A=a3, B=b1 ==> C=c2",
                          "A=a1, B=b1 ==> C=c3"]
        self.cols = ['rule print', 'ant_supp', 'con_supp', 'rule_supp', 'confidence', 'lift', '# of records']
        self.association_rules = pd.DataFrame.from_records([{'rule print':"A=a1 ==> B=b1", 'ant_supp': 5, 'con_supp': 6,
                                                         'rule_supp': 3, 'confidence': 3/5, 'lift': (3/5)/(6/10),
                                                         '# of all records': 10},
                                                         {'rule print': "A=a1 ==> B=b2", 'ant_supp': 5, 'con_supp': 2,
                                                           'rule_supp': 1, 'confidence': 1 / 5,
                                                           'lift': (1 / 5) / (2/10),
                                                           '# of all records': 10},
                                                         {'rule print': "A=a1 ==> B=b3", 'ant_supp': 5, 'con_supp': 2,
                                                          'rule_supp': 1, 'confidence': 1 / 5,
                                                          'lift': (1 / 5) / (2 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "A=a2 ==> B=b1", 'ant_supp': 2, 'con_supp': 6,
                                                            'rule_supp': 2, 'confidence': 1,
                                                            'lift': 1 / (6/10),
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
                                                           'rule_supp': 1, 'confidence': 1/3,
                                                           'lift': (1/3) / (2/10),
                                                           '# of all records': 10},
                                                         {'rule print': "B=b1 ==> A=a1", 'ant_supp': 6, 'con_supp': 5,
                                                          'rule_supp': 3, 'confidence': 3 / 6,
                                                          'lift': (3 / 6) / (5 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b1 ==> A=a2", 'ant_supp': 6, 'con_supp': 2,
                                                          'rule_supp': 2, 'confidence': 2/6,
                                                          'lift': (2/6) / (2 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b1 ==> A=a3", 'ant_supp': 6, 'con_supp': 3,
                                                          'rule_supp': 1, 'confidence': 1 / 6,
                                                          'lift': (1 / 6) / (3 / 10),
                                                          '# of all records': 10},
                                                          {'rule print': "B=b2 ==> A=a1", 'ant_supp': 2, 'con_supp': 5,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (5 / 10),
                                                          '# of all records': 10},
                                                          {'rule print': "B=b2 ==> A=a3", 'ant_supp': 2, 'con_supp': 3,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (3 / 10),
                                                          '# of all records': 10},
                                                          {'rule print': "B=b3 ==> A=a1", 'ant_supp': 2, 'con_supp': 5,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (5 / 10),
                                                          '# of all records': 10},
                                                          {'rule print': "B=b3 ==> A=a3", 'ant_supp': 2, 'con_supp': 3,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (3 / 10),
                                                               '# of all records': 10}], columns=self.cols)
        self.association_rules_pat = pd.DataFrame.from_records(
                                                        [{'rule print': "A=a2 ==> B=b1", 'ant_supp': 2, 'con_supp': 6,
                                                          'rule_supp': 2, 'confidence': 1,
                                                          'lift': 1 / (6 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "A=a3 ==> B=b1", 'ant_supp': 3, 'con_supp': 6,
                                                          'rule_supp': 1, 'confidence': 1 / 3,
                                                          'lift': (1 / 3) / (6 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "A=a3 ==> B=b3", 'ant_supp': 3, 'con_supp': 2,
                                                          'rule_supp': 1, 'confidence': 1 / 3,
                                                          'lift': (1 / 3) / (2 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b1 ==> A=a2", 'ant_supp': 6, 'con_supp': 2,
                                                          'rule_supp': 2, 'confidence': 2 / 6,
                                                          'lift': (2 / 6) / (2 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b1 ==> A=a3", 'ant_supp': 6, 'con_supp': 3,
                                                          'rule_supp': 1, 'confidence': 1 / 6,
                                                          'lift': (1 / 6) / (3 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b3 ==> A=a3", 'ant_supp': 2, 'con_supp': 3,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (3 / 10),
                                                          '# of all records': 10}], columns=self.cols)
        self.association_rules_dup = pd.DataFrame.from_records(
                                                        [{'rule print': "A=a1 ==> B=b1", 'ant_supp': 5, 'con_supp': 6,
                                                          'rule_supp': 3, 'confidence': 3 / 5, 'lift': (3 / 5) / (6 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "A=a2 ==> B=b1", 'ant_supp': 2, 'con_supp': 6,
                                                          'rule_supp': 2, 'confidence': 1,
                                                          'lift': 1 / (6 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "A=a3 ==> B=b1", 'ant_supp': 3, 'con_supp': 6,
                                                          'rule_supp': 1, 'confidence': 1 / 3,
                                                          'lift': (1 / 3) / (6 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b2 ==> A=a1", 'ant_supp': 2, 'con_supp': 5,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (5 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b2 ==> A=a3", 'ant_supp': 2, 'con_supp': 3,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (3 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b3 ==> A=a1", 'ant_supp': 2, 'con_supp': 5,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (5 / 10),
                                                          '# of all records': 10},
                                                         {'rule print': "B=b3 ==> A=a3", 'ant_supp': 2, 'con_supp': 3,
                                                          'rule_supp': 1, 'confidence': 1 / 2,
                                                          'lift': (1 / 2) / (3 / 10),
                                                          '# of all records': 10}], columns=self.cols)

        self.association_rules_part = self.association_rules.copy()
        self.association_rules_part['type'] = self.association_rules_part['rule print'].apply(lambda x: x.split('=')[0])
        self.association_rules_ants = self.association_rules_part[self.association_rules_part['type']=='A']
        self.deciles = pd.Series(10*[10],index=['1.0 - 10.0','10.0 - 20.0','20.0 - 30.0', '30.0 - 40.0', '40.0 - 50.0',
                                                '50.0 - 60.0', '60.0 - 70.0', '70.0 - 80.0','80.0 - 90.0', '90.0 - 100'])

    def test_create_variable_lists(self):
        all_none = ar._create_variable_lists(self.sample_df, list_of_ants=None, list_of_cons=None, list_of_cols=None)
        self.assertEqual(all_none[0],list(self.sample_df.columns),"Full list of ants was not extracted properly")
        self.assertEqual(all_none[1],list(self.sample_df.columns),"Full list of cons was not extracted properly")
        self.assertEqual(all_none[2],list(self.sample_df.columns),"Full list of cols was not extracted properly")

        ant_intersection = ar._create_variable_lists(self.sample_df, list_of_ants=['A'], list_of_cons=None,
                                                    list_of_cols=None)
        self.assertEqual(ant_intersection[0], ['A'], "Ant intersection list of ants was not extracted properly")
        self.assertEqual(ant_intersection[1], list(self.sample_df.columns),
                         "Ant intersection list of cons was not extracted properly")
        self.assertEqual(ant_intersection[2], list(self.sample_df.columns),
                         "Ant intersection list of cols was not extracted properly")
        con_intersection = ar._create_variable_lists(self.sample_df, list_of_ants=None, list_of_cons=['A'],
                                                    list_of_cols=None)
        self.assertEqual(con_intersection[0], list(self.sample_df.columns),
                         "Con intersection list of ants was not extracted properly")
        self.assertEqual(con_intersection[1], ['A'], "Con intersection list of cons was not extracted properly")
        self.assertEqual(con_intersection[2], list(self.sample_df.columns),
                         "Con intersection list of cols was not extracted properly")
        ant_and_con = ar._create_variable_lists(self.sample_df, list_of_ants=['A'], list_of_cons=['B'],
                                                    list_of_cols=None)
        self.assertEqual(ant_and_con[0], ['A'], "Ant and con list of ants was not extracted properly")
        self.assertEqual(ant_and_con[1], ['B'], "Ant and con list of cols was not extracted properly")
        self.assertEqual(set(ant_and_con[2]), set(['A','B']), "Ant and con list of cols was not extracted properly")

        with self.assertRaises(ValueError, msg="An external column sent with no exception"):
            ar._create_variable_lists(self.sample_df, list_of_ants=['G'], list_of_cons=None, list_of_cols=None)
        with self.assertRaises(ValueError, msg="An external column to the list iof columns was sent with no exception"):
            ar._create_variable_lists(self.sample_df, list_of_ants=['C'], list_of_cons=None, list_of_cols=['A','B'])
        with self.assertRaises(ValueError, msg="List of columns is not the union of subset lists with no exception"):
            ar._create_variable_lists(self.sample_df, list_of_ants=['A'], list_of_cons=['B'], list_of_cols=['A','B','C'])

    def test_create_list_of_formats(self):
        list_of_formats = ar._create_list_of_formats(max_rule_columns=4)
        self.assertEqual(set(list_of_formats),self.set_of_4_formats,"Formats were not built properly")

        list_of_formats = ar._create_list_of_formats(max_rule_columns=4, max_ant=1)
        self.assertEqual(set(list_of_formats), self.set_of_ant_1_formats, "Formats were not built properly")

        list_of_formats = ar._create_list_of_formats(max_rule_columns=4, max_con=1)
        self.assertEqual(set(list_of_formats), self.set_of_con_1_formats, "Formats were not built properly")

        with self.assertRaises(ValueError):
            ar._create_list_of_formats(max_rule_columns=1)

    def test_get_rules_by_format(self):
        list_of_rules = ar._get_variable_rules_by_format(self.list_of_cols,self.list_of_cols,(2,1))
        self_in_func = [(dict in list_of_rules) for dict in self.list_of_2_1_rules]
        self.assertEqual(sum(self_in_func),len(self_in_func), "Not all variable level rules were extracted")
        func_in_self = [(dict in self.list_of_2_1_rules) for dict in list_of_rules]
        self.assertEqual(sum(func_in_self), len(func_in_self), "There were redundant rules created")

        with self.assertRaises(ValueError):
            ar._get_variable_rules_by_format(self.list_of_cols,self.list_of_cols,(3,3))

    def test_get_sup_dictionary(self):
        sup_dict = ar._get_sup_dictionary(self.sample_df,['A','B','C'])
        self.assertEqual(set(sup_dict),self.set_of_sups, "Support dictionary does not contain the expected keys")
        np.testing.assert_array_equal(self.sup_A.values,sup_dict[frozenset('A')].values)

        with self.assertRaises(ValueError):
            ar._get_sup_dictionary(self.sample_df, ['A', 'B', 'E'])

    def test_create_rules(self):
        sup_dict = ar._get_sup_dictionary(self.sample_df,['A','B','C','D'])
        all_rules = ar._create_all_rules(self.variable_rule_list,sup_dict,0.01,10)
        extracted_rules = list(all_rules['rule print'])
        self.assertEqual(set(extracted_rules),set(self.rule_list), "Wrong rules were extracted")
        single_rule = all_rules[all_rules['rule print'] == "A=a1, B=b1 ==> C=c2"].squeeze()
        self.assertEqual(len(single_rule),12, "Some rule fields are missing")
        self.assertEqual(set(single_rule['antecedent']),{'A','B'},"antecedent was not calculated properly")
        self.assertEqual(set(single_rule['consequent']),{'C'},"antecedent was not calculated properly")
        self.assertEqual(single_rule['ant_count'],3,"'ant_supp' was not calculated properly")
        self.assertEqual(single_rule['ant_supp'],0.3,"'ant_supp' was not calculated properly")
        self.assertEqual(single_rule['con_count'],3,"'con_supp' was not calculated properly")
        self.assertEqual(single_rule['con_supp'],0.3,"'con_supp' was not calculated properly")
        self.assertEqual(single_rule['rule_count'],1,"'con_supp' was not calculated properly")
        self.assertEqual(single_rule['rule_supp'],0.1,"'con_supp' was not calculated properly")
        self.assertEqual(single_rule['confidence'],round(1/3,4),"'confidence' was not calculated properly")
        self.assertEqual(single_rule['lift'],round((1/3)/(3/10),4),"'lift' was not calculated properly")
        self.assertEqual(single_rule['# of all records'],10,"'# of all records' was not calculated properly")

    def test_check_column(self):
        test_df = pd.DataFrame(np.random.rand(1000,1),columns=['rand'])
        self.assertEqual(ar._check_column(test_df,'rand'),'bin',"Failed to identify column for binning")
        test_df['non-str'] = 1
        self.assertEqual(ar._check_column(test_df,'non-str'),'non-str',"Failed to identify a non-str column")
        test_df['str'] = 'test'
        self.assertEqual(ar._check_column(test_df,'str'),'str',"Failed to identify an str column")

    def test_drop_duplicates(self):
        ass_rules,_ = ar.create_association_rules(self.sample_df,['A','B'])
        ass_rules_dup = ar._drop_duplicates(ass_rules)
        self.assertEqual(set(self.association_rules_dup['rule print']) ,set(ass_rules_dup['rule print']),
                         "Dropping rule duplicate was not done properly")

    def test_validate_rules_df(self):
        ass_rules, _ = ar.create_association_rules(self.sample_df)
        self.assertTrue(ar._validate_rules_df(ass_rules))

    def test_clean_column_lists(self):
        list_of_cols = ['A','F']
        list_of_ants = ['A','F']
        list_of_cons = ['A']
        ar._clean_column_lists(self.sample_df, list_of_ants, list_of_cons, list_of_cols)
        self.assertEqual(list_of_cols,['A'],"List of cols was not cleaned properly")
        self.assertEqual(list_of_ants,['A'],"List of ants was not cleaned properly")
        self.assertEqual(list_of_cons,['A'],"List of cons was not cleaned properly")

    def test_alter_df(self):
        rand_array = np.random.rand(1000)
        test_df = pd.DataFrame(0, index=np.arange(1000),columns=['A','B'])
        test_df['C'] = rand_array
        ar._alter_df(test_df,['A','C'],None)
        self.assertEqual(list(test_df.columns),['A','B'],
                         "Data alteration - omit continuous column, was not done properly")
        self.assertEqual(type(test_df['A'][0]),str,"Data alteration - change non-str type, was not done properly")

        test_df['C'] = rand_array
        ar._alter_df(test_df, ['A', 'C'], five_quantile_based_bins)
        self.assertEqual(type(test_df['C'][0]), str, "Data alteration - bin continuous column, was not done properly")

