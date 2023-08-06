import pandas as pd
import numpy as np

eps=0.00001

def _create_labels(bins_for_labels: list, round_param: int):
    """
    This function receives a list of bin edges and a rounding parameter and returns a list of bin labels. The returned
    list is shorter by one element from the list of bins. The rounding parameter is used to round the bin edges.
    :param bins_for_labels:
    :param round_param:
    :return: list of string labels
    """
    bin_start = bins_for_labels[:-1]
    bin_end =  bins_for_labels[1:]
    labels = []
    for i in range(len(bin_start)):
        opener = '('
        closer= ']'
        if i == 0:
            opener = '['
        labels.append(opener + str(round(bin_start[i], round_param)) + " - " +
                      str(round(bin_end[i], round_param)) + closer)
    return labels


def _set_rounding_parameter(bins: list):
    """
    This function receives a list of bin edges and determines the minimal rounding parameter that will remain the
    rounded bin edges differentiated
    :param bins: list of bins
    :return: round parameter (integer
    """
    round_param = -1
    i = 0
    while round_param == -1:
        r_bins = set([round(b, i) for b in bins])
        if len(r_bins) == len(bins):
            round_param = i
        else:
            i += 1
    return round_param


def decile_based_bins(series: pd.Series):
    """
    This function receives a continuous pandas series and returns it mapped to decile bins.
    :param series: a pandas series to be b inned
    :return: binned pandas series
    """
    NUMBER_OF_BINS = 10
    basic_percentile = 100 / NUMBER_OF_BINS
    percentiles = list(np.arange(basic_percentile,100,basic_percentile))
    na_index = series.isna()
    valid_series = series[~na_index]
    na_series = series[na_index].fillna('Unknown')
    percentile_values = [np.percentile(valid_series,per,interpolation='lower') for per in percentiles]
    bins_for_labels = sorted(list(set([min(valid_series)] + percentile_values + [max(valid_series)])))
    bins = bins_for_labels.copy()
    bins[0] = bins[0] - eps
    bins[-1] = bins[-1] + eps
    round_param = _set_rounding_parameter(bins)
    labels = _create_labels(bins_for_labels, round_param)
    binned_series = pd.cut(valid_series, bins, labels=labels)
    attached_series = binned_series.append(na_series).reindex(series.index)
    return attached_series


def five_quantile_based_bins(series: pd.Series):
    """
    This function receives a continuous pandas series and returns it mapped to decile bins.
    :param series: a pandas series to be b inned
    :return: binned pandas series
    """
    basic_percentile = 100 / 5
    percentiles = list(np.arange(basic_percentile,100,basic_percentile))
    na_index = series.isna()
    valid_series = series[~na_index]
    na_series = series[na_index].fillna('Unknown')
    percentile_values = [np.percentile(valid_series,per,interpolation='lower') for per in percentiles]
    bins_for_labels = sorted(list(set([min(valid_series)] + percentile_values + [max(valid_series)])))
    bins = bins_for_labels.copy()
    bins[0] = bins[0] - eps
    bins[-1] = bins[-1] + eps
    round_param = _set_rounding_parameter(bins)
    labels = _create_labels(bins_for_labels, round_param)
    binned_series = pd.cut(valid_series, bins, labels=labels)
    attached_series = binned_series.append(na_series).reindex(series.index)
    return attached_series


def equal_value_range_bins_10(series: pd.Series):
    """
    This function receives a continuous pandas series and returns it mapped to bins. The bins are set by dividing the
    values range to equally sized ranges. The number of bins is predefined by the parameter : NUMBER_OF_BINS
    :param series:
    :return:
    """
    NUMBER_OF_BINS = 10
    na_index = series.isna()
    valid_series = series[~na_index]
    na_series = series[na_index].fillna('Unknown')
    max_val = valid_series.max()
    min_val = valid_series.min()
    cuts = list(np.arange(min_val, max_val, (max_val-min_val)/ NUMBER_OF_BINS))
    bins = sorted(list(set([min(valid_series)] + cuts[1:] + [max(valid_series)])))
    round_param = _set_rounding_parameter(bins)
    labels = _create_labels(bins,round_param)
    binned_series = pd.cut(valid_series, bins, labels=labels, include_lowest=True)
    attached_series = binned_series.append(na_series).reindex(series.index)
    return attached_series


def equal_value_range_bins_5(series: pd.Series):
    """
    This function receives a continuous pandas series and returns it mapped to bins. The bins are set by dividing the
    values range to equally sized ranges. The number of bins is predefined by the parameter : NUMBER_OF_BINS
    :param series:
    :return:
    """
    NUMBER_OF_BINS = 5
    na_index = series.isna()
    valid_series = series[~na_index]
    na_series = series[na_index].fillna('Unknown')
    max_val = valid_series.max()
    min_val = valid_series.min()
    cuts = list(np.arange(min_val, max_val, (max_val-min_val)/ NUMBER_OF_BINS))
    bins = sorted(list(set([min(valid_series)] + cuts[1:] + [max(valid_series)])))
    round_param = _set_rounding_parameter(bins)
    labels = _create_labels(bins,round_param)
    binned_series = pd.cut(valid_series, bins, labels=labels, include_lowest=True)
    attached_series = binned_series.append(na_series).reindex(series.index)
    return attached_series