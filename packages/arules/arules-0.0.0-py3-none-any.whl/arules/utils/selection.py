import pandas as pd
import numpy as np
from ..association_rules import _validate_rules_df


def _rules_by_var(rules: pd.DataFrame, var: frozenset):
    """
    This function filters an association rules dataframe by variable (keys of the antecedent dictionary_)
    :param rules: an association rules dataframe
    :param var: a frozenset of variables (strings)
    :return: filtered association rules df
    """
    filter_var = rules['antecedent'].apply(lambda x: var == frozenset(x.keys()))
    return rules[filter_var]


def top_bottom_20(rules_df: pd.DataFrame):
    """
    This function receives an association rules dataframe, and returns the 20 rules with the highest lift concatenated
    to the 20 rules with the lowest lift in a single dataframe. The function returns a tuple that contains the dataframe
    within a list (of 1 element) and the df title ('Rules with Most Significant Lift')
    :param rules_df: an association rules dataframe
    :return: a tuple of an association rules dataframe within a list and a title (string)
    """
    NUM_RULES = 20
    if not _validate_rules_df(rules_df):
        raise ValueError("The dataframe sent is not an association rules dataframe")
    if rules_df.shape[0] <= 2 * NUM_RULES:
        rules_to_present = [rules_df]
    else:
        extreme_rules = rules_df.head(NUM_RULES).append(rules_df.tail(NUM_RULES))
        rules_to_present = [extreme_rules]
    title = ['Rules with Most Significant Lift']
    return rules_to_present, title


def top_bottom_10(rules_df: pd.DataFrame):
    """
    This function receives an association rules dataframe, and returns the 10 rules with the highest lift concatenated
    to the 10 rules with the lowest lift in a single dataframe. The function returns a tuple that contains the dataframe
    within a list (of 1 element) and the df title ('Rules with Most Significant Lift')
    :param rules_df: an association rules dataframe
    :return: a tuple of an association rules dataframe within a list and a title (string)
    """
    NUM_RULES = 10
    if not _validate_rules_df(rules_df):
        raise ValueError("The dataframe sent is not an association rules dataframe")
    if rules_df.shape[0]<=2*NUM_RULES:
        rules_to_present = [rules_df]
    else:
        extreme_rules = rules_df.head(NUM_RULES).append(rules_df.tail(NUM_RULES))
        rules_to_present = [extreme_rules]
    title = ['Rules with Most Significant Lift']
    return rules_to_present, title


def top_10_variant_variables(rules_df: pd.DataFrame):
    """
    This function receives an association rules dataframe, and returns a list of association rules dataframes. Each
    dataframe contains rules of a single antecedent. The selected antecedents are those who form association rules
    dataframes with the highest lift variability (measured by standard deviation). The function returns a tuple that
    contains the dataframes within a list and the df titles (according to the selected variables)
    :param rules_df: an association rules dataframe
    :return: a tuple of an association rules dataframes within a list and a title list (strings)
    """
    NUM_RULES = 10
    if not _validate_rules_df(rules_df):
        raise ValueError("The dataframe sent is not an association rules dataframe")
    keys = lambda x: frozenset(rules_df['antecedent'].loc[x].keys())
    grouped_rules = rules_df[['antecedent', 'lift']].groupby(keys).apply(np.std)
    sorted_grouped_rules = grouped_rules.sort_values('lift', ascending=False)
    if sorted_grouped_rules.shape[0] > NUM_RULES:
        sorted_grouped_rules = sorted_grouped_rules.iloc[0:NUM_RULES]
    titles = [' , '.join(list(ant)) for ant in sorted_grouped_rules.index]
    rules_list = [_rules_by_var(rules_df, ant) for ant in sorted_grouped_rules.index]
    return rules_list, titles


def top_5_variant_variables(rules_df: pd.DataFrame):
    """
    This function receives an association rules dataframe, and returns a list of association rules dataframes. Each
    dataframe contains rules of a single antecedent. The selected antecedents are those who form association rules
    dataframes with the highest lift variability (measured by standard deviation). The function returns a tuple that
    contains the dataframes within a list and the df titles (according to the selected variables)
    :param rules_df: an association rules dataframe
    :return: a tuple of an association rules dataframes within a list and a title list (strings)
    """
    NUM_RULES = 5
    if not _validate_rules_df(rules_df):
        raise ValueError("The dataframe sent is not an association rules dataframe")
    keys = lambda x: frozenset(rules_df['antecedent'].loc[x].keys())
    grouped_rules = rules_df[['antecedent','lift']].groupby(keys).apply(np.std)
    sorted_grouped_rules = grouped_rules.sort_values('lift', ascending=False)
    if sorted_grouped_rules.shape[0] > NUM_RULES:
        sorted_grouped_rules = sorted_grouped_rules.iloc[0:NUM_RULES]
    titles = [' , '.join(list(ant)) for ant in sorted_grouped_rules.index]
    rules_list = [_rules_by_var(rules_df, ant) for ant in sorted_grouped_rules.index]
    return rules_list,titles


def specified_list_of_variables(list_of_vars: list):
    """
    This function receives a list of variables and returns a function that given an associationa rules dataframe will
    return a lists of association rules dataframes and titles according to the list of variables
    :param list_of_vars: list of variables, that are a subset of the antecendents of the association rules dataframe
    :return: rules selection function
    """
    def _specified_list_of_vars(rules_df: pd.DataFrame):
        """
        This function receives an association rules dataframe, and returns a list of association rules dataframes. Each
        dataframe contains rules of a single antecedent according to the list of variables from the oiuter function. The
        function returns a tuple that contains the dataframes within a list and the df titles (according to the list of
        variables from the oiuter function)
        :param rules_df: an association rules dataframe
        :return: a tuple of an association rules dataframes within a list and a title (string)
        """
        if not _validate_rules_df(rules_df):
            raise ValueError("The dataframe sent is not an association rules dataframe")
        titles = list_of_vars
        var_frozensets = [frozenset(var) for var in list_of_vars]
        rules_list = [_rules_by_var(rules_df, var) for var in var_frozensets]
        return rules_list,titles
    return _specified_list_of_vars