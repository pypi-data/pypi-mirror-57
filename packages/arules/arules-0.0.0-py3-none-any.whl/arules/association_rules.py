import pandas as pd
import numpy as np
import itertools
import tqdm
import sys
import re
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from typing import Callable
from IPython.display import display
# from .utils.selection import top_bottom_20
# import tabulate

RULES_DF_DTYPES = [dict, dict, str, int, int, int, float, float, float, float, float, int]
ALL_COLUMNS = ['antecedent','consequent','rule print', 'ant_count', 'con_count', 'rule_count', 'ant_supp', 'con_supp',
               'rule_supp', 'confidence', 'lift', '# of all records']
PRESENT_COLUMNS = ['rule print', 'ant_supp', 'con_supp', 'rule_supp', 'confidence', 'lift']
NUMBER_OF_VALUES = 15
VALUES_RATIO = 0.05



def _validate_tuple(x):
    """
    This function gets any type of object and returns it within a single element tuple. If the element is already a
    tuple it returns the element itself
    :param x: element
    :return: tuple
    """
    if type(x)!=tuple:
        return (x,)
    else:
        return x


def _create_list_of_formats(max_rule_columns: int, max_ant: int=float("inf"), max_con: int=float("inf")):
    """
        Create all possible rule formats according to the specifications. A rule format is a tuple with a length of 2,
        the first slot is for the rule's antecedent set size and the second slot is for the rule's consequent.
        :param max_rule_columns: maximal size of rule set (antecedent + consequent)
        :param max_ant: maximal size of antecedent set
        :param max_con: maximal size of consequent set
        :return: list of formats (tuples)
        """
    if max_rule_columns<=1:
        raise ValueError("Cannot create formats of less than 2 elements")
    list_of_formats = []
    for i in range(max_rule_columns - 1):
            list_of_formats = list_of_formats + [(j + 1, i - j + 1) for j in range(i + 1)
                                                 if np.logical_and(j<max_ant,(i-j)<max_con)]
    return list_of_formats


def _get_variable_rules_by_format_old(list_of_cols: list, rule_format: tuple):
    """
           Creates all the variable level rules following the specified format. Every rule is a dictionary that contains
           the set of variables of the antecedent and the set of variables of the consequent.
           :param list_of_colsl: list of column names upon which the format should be applied
           :param rule_format: sets the desired amount of variables to be used for antecedent and the consequent.
           :return: list of rules (dictionaries)
           """
    if sum(rule_format)>len(list_of_cols):
        raise ValueError("# of columns does not match the format ")
    list_of_ants = itertools.combinations(list_of_cols, rule_format[0])
    list_of_rules = []
    for ant in list_of_ants:
        list_of_cons = list(itertools.combinations(list_of_cols, rule_format[1]))
        list_of_rules = list_of_rules + [{'ant': list(ant), 'con': list(con)} for con in list_of_cons if
                                         len(set(ant) & set(con)) == 0]
    return list_of_rules


def _get_variable_rules_by_format(list_of_ants: list, list_of_cons:list, rule_format: tuple):
    """
           Creates all the variable level rules following the specified format. Every rule is a dictionary that contains
           the set of variables of the antecedent and the set of variables of the consequent.
           :param list_of_ants: list of column names upon which the antecedent format should be applied
           :param list_of_cons: list of column names upon which the consequent format should be applied
           :param rule_format: sets the desired amount of variables to be used for antecedent and the consequent.
           :return: list of rules (dictionaries)
           """

    if rule_format[0]>len(list_of_ants):
        raise ValueError("# of antecedent columns does not match the format ")
    if rule_format[1]>len(list_of_cons):
        raise ValueError("# of consequent columns does not match the format ")
    if sum(rule_format)>len(set(list_of_ants+list_of_cons)):
        raise ValueError("# of columns does not match the format ")
    list_of_ant_combs = itertools.combinations(list_of_ants, rule_format[0])
    list_of_rules = []
    for ant in list_of_ant_combs:
        list_of_con_combs = list(itertools.combinations(list_of_cons, rule_format[1]))
        list_of_rules = list_of_rules + [{'ant': list(ant), 'con': list(con)} for con in list_of_con_combs if
                                         len(set(ant) & set(con)) == 0]
    return list_of_rules


def _get_support(df: pd.DataFrame, element: frozenset, remove_patterns: dict):
    """
    This function returns the support Series of a set of columns w.r.t. a dataframe. If some columns have unwanted
    patterns it omits them.
    :param df: the dataframe over which the supports are calculated
    :param element: set of columns
    :param remove_patterns: a dictionary of unwanted patterns by columns
    :return: pandas series of the feature level supports
    """
    support = df.groupby(list(element)).size()
    intersection = [val for key, val in remove_patterns.items() if key in element]
    if len(intersection)>0:
        if len(element)>1:
            for i in range(len(support.index.levels)):
                if support.index.names[i] in remove_patterns:
                    new_labels = [label for label in support.index.levels[i] if re.match(remove_patterns[support.index.names[i]], label) is None]
                    support = support[support.index.get_level_values(support.index.names[i]).isin(new_labels)]
        else:
            new_labels = [label for label in support.index if re.match(remove_patterns[list(element)[0]], label) is None]
            support = support[support.index.isin(new_labels)]
    return support


def _get_sup_dictionary(df: pd.DataFrame, list_of_cols: list, max_cols: int=float("inf"), remove_patterns: dict={}):
    """
               Creates a dictionary of supports. Keys are sets of variables and are created according to all the
               possible combinations that meets the size limitation.
               :param df: the actual data set
               :param list_of_cols: the columns that should be used for the supports calculations
               :param max_cols: size limitation for the support sets
               :param remove_patterns: by variable dictionary of patterns to exclude
               :return: dictionary of support by column sets
               """
    if not (set(list_of_cols) <= set(df.columns)):
        not_in_columns = [col for col in list_of_cols if col not in df.columns]
        raise ValueError("The columns: " + ", ".join(not_in_columns) + ", do not appear in the dataframe")
    list_of_sups = []
    actual_max_cols = min(max_cols,len(list_of_cols))
    for i in range(actual_max_cols):
        list_of_sups = list_of_sups + list(itertools.combinations(list_of_cols, i + 1))

    set_of_sups = [frozenset(el) for el in list_of_sups]
    print("Calculating all relevant supports")
    sup_dict = {el: _get_support(df, el, remove_patterns) for el in tqdm.tqdm(set_of_sups, file=sys.stdout)}
    return sup_dict


def _create_all_rules(variable_rule_list: list, sup_dictionary: dict, min_supp: float, num_records: int):
    """
               Creates a dataframe of all the rules that can be extracted from each of the variable level rules in the
               list of rules. Rules that don't meet he min support threshold are filtered.
               :param variable_rule_list: list of variable level rules (dictionaries)
               :param sup_dictionary: dictionary of support by column sets
               :param min_supp: minimal support limitation
               :param num_records: overall number of records (transactions)
               :return: a dataframe that contains all the rules and their stats
               """
    all_rules_list = []
    print("\n"+"Calculating all feature level rules per variable level rule")
    for rule in tqdm.tqdm(variable_rule_list, file=sys.stdout):
        try:
            ant_supp_full = sup_dictionary[frozenset(rule['ant'])]
            con_supp_full = sup_dictionary[frozenset(rule['con'])]
            rule_supp_full = sup_dictionary[frozenset(rule['ant'] + rule['con'])]
        except KeyError as ke:
            print("Some of the required rules values do not appear in the support dictionary")
            raise ke

        if ant_supp_full.index.names != rule['ant']:
            ant_supp_full = ant_supp_full.reorder_levels(rule['ant'])
        if con_supp_full.index.names != rule['con']:
            con_supp_full = con_supp_full.reorder_levels(rule['con'])
        rule_list = rule['ant'] + rule['con']
        if rule_supp_full.index.names != rule_list:
            rule_supp_full = rule_supp_full.reorder_levels(rule_list)
        ant_supp_all = ant_supp_full[ant_supp_full / num_records >= min_supp]
        con_supp_all = con_supp_full[con_supp_full / num_records >= min_supp]
        rule_supp_all = rule_supp_full[rule_supp_full / num_records >= min_supp]

        index_set = set(rule_supp_all.index)
        rules_list = []
        for feature_rule in itertools.product(ant_supp_all.index, con_supp_all.index):
            rule_tup = _validate_tuple(feature_rule[0]) + _validate_tuple(feature_rule[1])
            if rule_tup in index_set:
                ant_count = ant_supp_all[feature_rule[0]]
                ant_supp = ant_count/num_records
                con_count = con_supp_all[feature_rule[1]]
                con_supp = con_count/num_records
                rule_count = rule_supp_all[rule_tup]
                rule_supp = rule_count/num_records
                confidence = round(rule_count / ant_count, 4)
                lift = round((rule_count / ant_count) / (con_count / num_records), 4)
                antecedent = {var: feat for var, feat in zip(ant_supp_all.index.names, _validate_tuple(feature_rule[0]))}
                consequent = {var: feat for var, feat in zip(con_supp_all.index.names, _validate_tuple(feature_rule[1]))}
                ant_print = ', '.join(
                    [var + "=" + feat for var, feat in zip(ant_supp_all.index.names, _validate_tuple(feature_rule[0]))])
                con_print = ', '.join(
                    [var + "=" + feat for var, feat in zip(con_supp_all.index.names, _validate_tuple(feature_rule[1]))])
                rule_print = ant_print + " ==> " + con_print
                rules_list.append([antecedent, consequent, rule_print, ant_count, con_count, rule_count, ant_supp,
                                   con_supp, rule_supp, confidence, lift, num_records])
        all_rules_list = all_rules_list + rules_list
    all_rules = pd.DataFrame(all_rules_list, columns=ALL_COLUMNS)
    return all_rules


def _dup_str(rule_print: str):
    """
    This function returns a string of all the features used in a rule alphabetically ordered separated by commas
    :param rule_print: a string of rule in the rule print format
    :return: the above mentioned string
    """
    return ','.join(sorted(list(itertools.chain.from_iterable([el.split(',') for el in rule_print.split(' ==> ')]))))


def _drop_duplicates(rules_df: pd.DataFrame):
    """
    This function gets an association rules dataframe and omits symmetric rules with lower confidence
    :param rules_df: association rules dataframe
    :return: deduped associations df
    """
    rules_df_copy = rules_df.copy()
    rules_df_copy['dups_str'] = rules_df_copy['rule print'].apply(lambda x: _dup_str(x))
    deduped_rules = rules_df_copy.drop_duplicates(['dups_str','lift','rule_supp']).reset_index(drop=True)
    return deduped_rules.drop('dups_str',axis=1)


def _check_column(df: pd.DataFrame, col: str):
    """
    This function receives a dataframe and a column within it, and examine whether the column is continuous.
    The continuity determination is done by threshold policy, where the main characteristics being examined is the type
    of data and the ratio between the number of unique values and the overall number of values
    :param df: Pandas dataframe to examine
    :param col: A columns within the dataframe
    :return: boolean value - True if the column is con sidered to be continuous
    """
    num_vals = len(df[col].value_counts())
    if (type(df[col].iloc[0])==str):
        col_dtype = 'str'
    elif (df[col].dtype in [int,float]) & (num_vals >= NUMBER_OF_VALUES) & (num_vals/df.shape[0]>=VALUES_RATIO):
            col_dtype = 'bin'
    else:
        col_dtype = 'non-str'
    return col_dtype


def create_association_rules(df: pd.DataFrame, list_of_cols: list=None, list_of_ants: list=None,
                             list_of_cons: list=None,list_of_formats: list=None, max_cols: int=float("inf"),
                             max_ant: int=float("inf"), max_con: int=float("inf"), min_supp: float=0.01,
                             remove_patterns: dict={}, supp_dict: dict=None, binning_method: Callable=None):
    """
                   This function returns association rules over tabular data. Variables are assumed to be categorical
                   and the rules are extracted in the variable-values (features) level. Each rule contains a string
                   representation of the rule ("antecedent ==> consequent") and the following stats: antecedent support,
                   consequent support, rule support, confidence, lift and overall number of records. The list of rules
                   can be controlled
                   :param df: the actual data set
                   :param list_of_cols: the columns that should be used for the rules calculations
                   :param list_of_ants: the columns that should be used for the rules antecedent
                   :param list_of_cons: the columns that should be used for the rules consequent
                   :param list_of_formats: list of desired rule formats
                   :param max_cols: size limitation for automatic format creation
                   :param max_ant: antecedent size limitation for automatic format creation
                   :param max_con: consequent size limitation for automatic format creation
                   :param min_supp: minimal support limitation
                   :param remove_patterns: by variable dictionary of patterns to exclude
                   :param supp_dict: dictionary of supports by column sets
                   :param binning_method: a functio according to which binnable columns will be divided.
                   :return: a dataframe that contains all the rules and their stats
                   """
    num_records = df.shape[0]
    list_of_ants, list_of_cons, list_of_cols = _create_variable_lists(df, list_of_ants, list_of_cons, list_of_cols)

    max_ant = min(max_ant, len(list_of_ants))
    max_con = min(max_con, len(list_of_cons))

    df_copy = df.copy()

    _alter_df(df_copy, list_of_cols, binning_method)

    _clean_column_lists(df_copy, list_of_ants, list_of_cons, list_of_cols)

    max_rule_columns = min(max_cols,max_ant+max_con, len(list_of_cols))
    if list_of_formats is None:
        list_of_formats = _create_list_of_formats(max_rule_columns, max_ant, max_con)
    max_rule_columns = min(max_cols,max_ant+max_con, len(list_of_cols),max([sum(tup) for tup in list_of_formats]))

    list_of_rules = []
    for rule_format in list_of_formats:
        list_of_rules = list_of_rules + _get_variable_rules_by_format(list_of_ants, list_of_cons, rule_format)

    if supp_dict is None:
        supp_dict = _get_sup_dictionary(df_copy, list_of_cols, max_rule_columns, remove_patterns)
    all_rules = _create_all_rules(list_of_rules, supp_dict, min_supp, num_records).sort_values(['lift', 'confidence'],
                                                                                               ascending=False)
    if all_rules.shape[0]==0:
        raise ValueError("Pattern dictionary has omitted all rules")
    print("Overall # of Rules: ", all_rules.shape[0])
    return all_rules.reset_index(drop=True), supp_dict


def _clean_column_lists(df: pd.DataFrame, list_of_ants: list, list_of_cons: list, list_of_cols: list):
    """
    This function cleans lists of columns according to the presence of the columns in the dataframe. It receives a
    dataframe and the list of columns and cleans the lists of columns.
    :param df: the actual data set
    :param list_of_cols: the columns that should be used for the rules calculations
    :param list_of_ants: the columns that should be used for the rules antecedent
    :param list_of_cons: the columns that should be used for the rules consequent
    :return: Null
    """
    cols_to_remove = [col for col in list_of_cols if col not in df.columns]
    for col in cols_to_remove:
        list_of_cols.remove(col)
        if col in list_of_ants:
            list_of_ants.remove(col)
        if col in list_of_cons:
            list_of_cons.remove(col)


def _alter_df(df: pd.DataFrame, list_of_cols: list, binning_method: Callable):
    """
    This function alters the a df to be compatible with the association rules requirements. It receives the df, list of
    columns and a binning method, examines the variable types of each of the columns and performs the required
    alteration: if the variable is dichotomous then no change is applied, if it is continuous it is binned according to
    the binning method, and if it is numerical with sporacic values it is simply altered to strings
    :param df: the actual data set
    :param list_of_cols: the columns that should be used for the rules calculations
    :param binning_method: a functio according to which binnable columns will be divided.
    :return: Null
    """
    column_types = {col: _check_column(df, col) for col in list_of_cols}
    for col, col_dtype in column_types.items():
        if col_dtype == 'str':
            continue
        elif col_dtype == 'non-str':
            df[col] = df[col].astype(str)
        elif col_dtype == 'bin':
            if binning_method is None:
                df.drop(col, inplace=True, axis=1)
            else:
                df[col] = binning_method(df[col])


def _create_variable_lists(df: pd.DataFrame, list_of_ants: list=None, list_of_cons: list=None, list_of_cols: list=None):
    """
    This function receives the dataframe, and the any set of the variable lists. It validates the given lists w.r.t. the
    data and themselves and creates the remaining lists as required.
    :param df: the actual data set
    :param list_of_ants: the columns that should be used for the rules antecedent
    :param list_of_cons: the columns that should be used for the rules consequent
    :param list_of_cols: the columns that should be used for the rules calculations
    :return: a tuple with all the extracted valid lists (ants, cons, cols)
    """
    if list_of_ants is not None and list_of_cons is not None:
        if list_of_cols is not None and not set(list_of_ants + list_of_cons) == set(list_of_cols):
            raise ValueError("List of columns is not the combination of the list of ants and the list of cons")
        else:
            list_of_cols = list(set(list_of_ants + list_of_cons))
    if list_of_cols is None:
        list_of_cols = list(df.columns)
    elif not (set(list_of_cols) <= set(df.columns)):
        not_in_columns = [col for col in list_of_cols if col not in df.columns]
        raise ValueError("The columns: " + ", ".join(not_in_columns) + ", from the list of columns, do not appear in "
                                                                       "the dataframe")
    if list_of_ants is not None:
        if not (set(list_of_ants) <= set(list_of_cols)):
            not_in_columns = [col for col in list_of_ants if col not in list_of_cols]
            raise ValueError("The columns: " + ", ".join(not_in_columns) + ", from the list of ants, do not appear in "
                                                                           "the overall list of columns")
    else:
        list_of_ants = list_of_cols

    if list_of_cons is not None:
        if not (set(list_of_cons) <= set(list_of_cols)):
            not_in_columns = [col for col in list_of_cons if col not in list_of_cols]
            raise ValueError("The columns: " + ", ".join(not_in_columns) + ", from the list of cons, do not appear in "
                                                                           "the overall list of columns")
    else:
        list_of_cons = list_of_cols
    return list_of_ants, list_of_cons, list_of_cols


def plot_rules(var_rules, title):
    """
    This function plots an association rules bar chart
    :param var_rules: an association rules dataframe
    :param title: the barchart title
    :return: Null
    """
    first_color = '#0303B4'
    second_color = '#00013A'
    third_color = '#C6EDFF'
    number_of_rules = var_rules.shape[0]
    df_to_plot = var_rules[['rule print','lift','ant_supp']].copy()
    df_to_plot['new_lift'] = df_to_plot['lift'].apply(lambda x: x if x>1 else 1/x )
    df_to_plot['new_lift_color'] = df_to_plot['lift'].apply(lambda x: x if x>1 else -1/x )
    df_to_plot['print'] = df_to_plot.apply(lambda x: x['rule print'].split('==>')[0] + ' | ' + str(int(100*x['ant_supp'])) + '%', axis=1 )
    df_to_plot = df_to_plot[['print','new_lift','new_lift_color']].set_index('print')
    present_data =df_to_plot.sort_values('new_lift_color',ascending=True)
    plt.figure(figsize=(12,number_of_rules))
    axes = plt.gca()
    axes.set_xlim(1, 1.1*df_to_plot['new_lift'].max())
    axes.set_xlabel('Lift',fontsize=20)
    labs = axes.get_xticks()
    labs_x = ['X'+ str(np.round(lab,1)) for lab in labs]
    axes.set_xticklabels(labs_x)
    bars = plt.barh(present_data.index,width=present_data['new_lift'], )
    for i in range(number_of_rules):
        if present_data['new_lift_color'].iloc[i]>1:
            bars[i].set_color(first_color)
        elif present_data['new_lift_color'].iloc[i]<-1:
            bars[i].set_color(second_color)
        else:
            bars[i].set_color(third_color)

    legend_elements = [Patch(facecolor=first_color, edgecolor=first_color,label='More Likely'),
                       Patch(facecolor=second_color, edgecolor=second_color,label='Less Likely')]
    plt.title(title, fontsize=30)
    plt.legend(legend_elements,['More Likely', 'Less Likely'],loc='center right',fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.show()



def _validate_rules_df(df: pd.DataFrame):
    """
    This function validates that a pandas dataframe is an association rules dataframe. It validates the columns and the
    data types within each column
    :param df: pandas dataframe
    :return: a boolean response. True means that i is indeed an association rukles dataframe
    """
    if not (set(df.columns) == set(ALL_COLUMNS)):
        return False
    check_types = df[ALL_COLUMNS].apply(lambda x: [type(el) for el in x]==RULES_DF_DTYPES,axis=1)
    if check_types.sum() < df.shape[0]:
        return False
    return True


def present_rules_per_consequent(rules_df: pd.DataFrame, consequent: dict, plot: bool=False, drop_dups: bool=False,
                                 selection_function: Callable=None):
    """
    This function prints and potentially visualize association rules w.r.t. a specific consequent. It prints a cleaner
    version of the associatiopn rules dataframe with configurable parameters (namely - confidence duplicate removal, and
    rules barchart). The selection of rules to present is done by a selection function, and he final response is a list
    of he association rules dataframe along with their repective titles
    :param rules_df: an association rules dataframe
    :param consequent: a single consequent to filter the rules according to
    :param plot: boolean parameter to set whether to plot rules barcharts
    :param drop_dups: determine whether to omit symmetric rules with lower confidence
    :param selection_function: a filtering function to select the antecedents of interest
    :return: a tuple of an association rules dataframes within a list and a title list (strings)
    """
    if not _validate_rules_df(rules_df):
        raise ValueError("The dataframe sent is not an association rules dataframe")

    rules_df_con = rules_df[rules_df['consequent']==consequent]
    if drop_dups:
        rules_df_con = _drop_duplicates(rules_df_con)
    list_of_rules_to_present, list_of_titles = selection_function(rules_df_con)

    for i in range(len(list_of_rules_to_present)):
        print(list_of_titles[i])
        display(list_of_rules_to_present[i][PRESENT_COLUMNS])
        if plot:
            plot_rules(list_of_rules_to_present[i][PRESENT_COLUMNS],list_of_titles[i])
