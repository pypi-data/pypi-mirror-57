# for credit score report
import pandas as pd


def split_score(scores, by='equal_width', n_splits=12):
    """
    Args:
        scores, a pandas Series
        by:
            equal_width,the whole range of scores is divided into a pre-specified number of equal-width intervals.
            equal_size,more or less equal number of observations.
        n_splits:
    Returns:
        score intervals,a list with Interval
    """
    max_score = scores.max()
    min_score = scores.min()
    if by == 'equal_width':
        size = int((max_score - min_score) / n_splits)
        score_cat = pd.cut(scores, size + 1, precision=0)
        score_interval_lst = list(set(score_cat))
        if len(score_interval_lst) > n_splits:
            pass
        elif len(score_interval_lst) < n_splits:
            pass
        return list(set(score_cat))
    elif by == 'equal_size':
        pass
