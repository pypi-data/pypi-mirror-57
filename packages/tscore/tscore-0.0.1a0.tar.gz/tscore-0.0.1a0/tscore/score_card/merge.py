import pandas as pd
import numpy as np


def _calc_chi_square_value(features, target):
    """
    Args:
        features,pandas DataFrame,
    """
    col_name = features.name
    target_name = target.name
    frame = pd.concat((features, target), axis=1)
    total_badrate = sum(target) / len(target)
    true_bad = frame.groupby(col_name)[target_name].sum()
    total = frame.groupby(col_name)[target_name].count()
    true_good = total - true_bad
    expected_bad = total * total_badrate
    expected_good = total - expected_bad
    chi_square_value = (np.square(true_good - expected_good) / expected_good +
                        np.square(true_bad - expected_bad) / expected_bad).sum()

    return chi_square_value


def _chi_merge(features, target, n_bins=5, min_threshold=4.8):
    """chi-merge
    Args:
        features,
        target,
        bins,numbers of bins to be merged
        min_samples,
        min_threshold,

    Returns:
        split array
    """
    # NULL values not merge
    features = features[features.notnull()]
    feature_unique = sorted((list(set(features))))
    if len(feature_unique) > 100:
        feature_unique_group = []
        out, bins = pd.qcut(feature_unique, 100, retbins=True)
        intervals = out.categories
        for i in intervals:
            feats_lst = []
            for feat in feature_unique:
                if i.left <= feat < i.right:
                    feats_lst.append(feat)
            feature_unique_group.append(feats_lst)
    else:
        feature_unique_group = [[feat] for feat in feature_unique]
    while len(feature_unique_group) > n_bins:
        split = [feature_unique_group[i] + feature_unique_group[i + 1] for i in range(len(feature_unique_group) - 1)]
        chi_square_value_lst = []
        for f in split:
            group_features = features[(features == f[0]) | (features == f[1])]
            chi_square_value = _calc_chi_square_value(group_features, target)
            chi_square_value_lst.append(chi_square_value)
        min_chi_index = chi_square_value_lst.index(min(chi_square_value_lst))
        feature_unique_group[min_chi_index] = feature_unique_group[min_chi_index] + feature_unique_group[min_chi_index+1]
        feature_unique_group.remove(feature_unique_group[min_chi_index + 1])

    split = [max(s) for s in feature_unique_group[:-1]]
    return split


def chi_merge(features, target, n_bins=5, min_samples=0.05, min_threshold=4.8, balance=True):
    """
    Args:
        features,
        target,
        n_bins
    Returns:
    """
    # the chi-square merge origin version
    split = _chi_merge(features, target, n_bins=n_bins)
    print(f'split is {split}')

    # if min bin samples < min_samples
    bad_rate = _bin_badrate(features, target, split)
    print(f'82 bad_rate is {bad_rate}')

    if balance:
        bl = np.square(bad_rate['bin_rate']).sum()
        print(f'bl is {bl}')
        if isinstance(min_samples, int):
            bad_rate = bad_rate[bad_rate['intervals'].notnull()]
            if (bad_rate['totals'] <= min_samples).any():
                print(f'the min_samples not satisfy statistical significance')
        elif isinstance(min_samples, float):
            bad_rate = bad_rate[bad_rate['intervals'].notnull()]
            while (bad_rate['bin_rate'] <= min_samples).any():
                print(f'the min_samples not satisfy statistical significance')
                nsss = bad_rate[bad_rate['bin_rate'] <= min_samples][['bins', 'intervals']]
                nsss_dict = nsss.set_index('bins').T.to_dict('records')[0]
                nsss_bins = sorted(list(nsss_dict.keys()), reverse=True)
                bin = nsss_bins[0]
                print(f'bin is {bin}')
                print(f'bad_rate is {bad_rate}')
                print(f'intervals is :')
                try:
                    left_bin_interval = bad_rate[bad_rate['bins'] == bin -1]['intervals'].iloc[0]  # nsss_dict[bin - 1]
                except (KeyError, IndexError):
                    left_bin_interval = None
                try:
                    right_bin_interval = bad_rate[bad_rate['bins'] == bin + 1]['intervals'].iloc[0]  # nsss_dict[bin + 1]
                except (KeyError, IndexError):
                    right_bin_interval = None
                print(f'left_bin_interval is {left_bin_interval}')
                print(f'right_bin_interval is {right_bin_interval}')
                if not pd.isnull(left_bin_interval) and pd.isnull(right_bin_interval):
                    print(f'left_bin_interval is {left_bin_interval}')
                    print(f'right_bin_interval is {right_bin_interval}')
                    left = left_bin_interval.left
                    # right = nsss_dict[bin].right
                    right = bad_rate[bad_rate['bins'] == bin]['intervals'].iloc[0].right
                elif not pd.isnull(right_bin_interval) and pd.isnull(left_bin_interval):
                    print(f'left_bin_interval is {left_bin_interval}')
                    print(f'right_bin_interval is {right_bin_interval}')
                    # left = nsss_dict[bin].left
                    left = bad_rate[bad_rate['bins'] == bin]['intervals'].iloc[0].left
                    right = right_bin_interval.right
                elif not pd.isnull(left_bin_interval) and pd.isnull(right_bin_interval):
                    print(f'left_bin_interval is {left_bin_interval}')
                    print(f'right_bin_interval is {right_bin_interval}')
                    left = left_bin_interval.left
                    right = right_bin_interval.right
                new_interval = pd.Interval(left=left, right=right, closed='right')
                original_intervals = bad_rate['intervals'].tolist()
                remove_intervals = original_intervals[bin]
                if new_interval.left == nsss_dict[bin].left:
                    remove_next_intervals = original_intervals[bin + 1]
                    original_intervals.remove(remove_next_intervals)
                else:
                    remove_last_intervals = original_intervals[bin - 1]
                    original_intervals.remove(remove_last_intervals)
                original_intervals.remove(remove_intervals)
                original_intervals.append(new_interval)
                new_splits = []
                for interval in original_intervals:
                    if not isinstance(interval, pd._libs.interval.Interval):
                        continue
                    if interval.left != -np.inf:
                        new_splits.append(interval.left)
                bad_rate = _bin_badrate(features, target, new_splits)
                print(f'new_splits is {new_splits}')
                if len(new_splits) > 2:
                    break
        else:
            raise Exception("Could not support %s type for variable min_samples" % type(min_samples))

    # if all is goods or bads,merge
    if (bad_rate['goods'] == 0).any(axis=None) or (bad_rate['bads'] == 0).any(axis=None):
        print('all is goods or bads !')
        if (bad_rate['goods'] == 0).any(axis=None):
            intervals_zero = bad_rate[bad_rate['goods'] == 0]['intervals'].tolist()
            print(f'interval {intervals_zero} goods is 0')
        if (bad_rate['bads'] == 0).any(axis=None):
            intervals_zero = bad_rate[bad_rate['bads'] ==0 ]['intervals'].tolist()
            print(f'interval {intervals_zero} bads is 0')

        # if is_monotone = False,then merge the bins
        is_monotone = _badrate_monotone(features, target, split)
        if not is_monotone:
            pass
    return split


def best_ks_merge():
    """
    Args:

    Returns:
    """
    pass


def _badrate_monotone(features, target, bins):
    """ get the monotone of features badrate
    Args:
        features,a Pandas DataFrame or Series of feature
        target,a Pandas DataFrame or Series of target variable
    Returns:
        if the badrate is monotone, then return True,else return False
    """
    if len(set(features)) <= 2:
        return True
    badrate = _bin_badrate(features, target, bins)
    badrate = badrate[badrate['intervals'].notnull()].sort_values(by='bins')
    bad_rate_lst = list(badrate['bad_rate'])
    i = 0
    if bad_rate_lst[i] <= bad_rate_lst[i+1]:
        flag = 'ASC'
    else:
        flag = 'DESC'
    last_br = bad_rate_lst[i+1]
    for index, br in enumerate(bad_rate_lst):
        if index == 0 or index == 1:
            continue
        elif flag == 'ASC' and br <= last_br:
            return False
        elif flag == 'DESC' and br >= last_br:
            return False
        last_br = br
    if last_br == bad_rate_lst[-1]:
        return True


def _bin_badrate(features, target, bins):
    """get the badrate of every bin
    Args:
        features,a pandas DataFrame or Series of a feature
        target,a pandas DataFrame or Series of the target variable
        bins,split intervals,for example,[0,3,5] represents {x <= 0 U 0 < x <= 3 U 3< x <= 5 U  x > 5}
    Returns:
        frame,a pandas DataFrame include columns ['var','bins','intervals','goods','bads','totals','bad_rate','bin_rate']
    """
    df = pd.concat((features, target), axis=1)
    frame = pd.DataFrame(columns=['var', 'bins', 'intervals', 'goods', 'bads',
                                  'totals', 'bad_rate', 'bin_rate'])
    frame['var'] = [features.name] * (len(bins) + 1 + 1)
    bins.append(np.inf)
    intervals_lst = [pd.Interval(left=-np.inf, right=bins[index], closed='right') if index == 0 else (
                     pd.Interval(left=s, right=np.inf, closed='left') if index == len(bins) else
                     pd.Interval(left=bins[index - 1], right=s, closed='right')
    ) for index, s in enumerate(bins)]
    bins.remove(np.inf)
    intervals_lst.append(np.nan)
    frame['intervals'] = intervals_lst
    frame['bins'] = frame['intervals'].apply(lambda r: len(bins) + 1 if pd.isnull(r) else (bins.index(r.right) if r.right is not np.inf
                                                                           else len(bins)))
    frame['goods'] = frame['intervals'].apply(lambda r: len(df[(df[features.name].isnull()) &
                                                               (df[target.name] == 0)]) if pd.isnull(r)
                                                           else len(df[(df[features.name] <= r.right) &
                                                           (df[features.name] > r.left) &
                                                           (df[target.name] == 0)])
                                              )
    frame['bads'] = frame['intervals'].apply(lambda r: len(df[(df[features.name].isnull()) &
                                                               (df[target.name] == 1)]) if pd.isnull(r)
                                                           else len(df[(df[features.name] <= r.right) &
                                                           (df[features.name] > r.left) &
                                                           (df[target.name] == 1)])
                                              )
    frame['totals'] = frame['intervals'].apply(lambda r: len(df[(df[features.name].isnull())]) if pd.isnull(r)
                                                           else len((df[(df[features.name] <= r.right) &
                                                           (df[features.name] > r.left)])))
    frame['bad_rate'] = frame['bads'] * 1.0 / frame['totals']
    frame['bin_rate'] = frame['totals'].apply(lambda r: r * 1.0 / len(df))
    return frame


# if __name__ == '__main__':
#     df = pd.read_csv('../datasets/train_v0_2_add_new_zx.csv', encoding='gbk')
#     df = df[df['是否违约'] != 2]
#     df = df.round(3)
#     # chi_square_value = _calc_chi_square_value(df['过多征信查询'], df['是否违约'])
#     # print(f'chi_square_value is {chi_square_value}')
#     feat_lst = ['近六月平均数字解读'] # ['过多征信查询']  # ['近六月平均数字解读']
#     for feat in feat_lst:
#         print('it is running')
#         split = chi_merge(df[feat], df['是否违约'], n_bins=5)
#         print(f'split is {split}')
#
#         frame = _bin_badrate(df[feat], df['是否违约'], bins=split)
#         print(f'frame is {frame}')
#
#         is_monotone = _badrate_monotone(df[feat], df['是否违约'], bins=split)
#         print(f'is_monotone is {is_monotone}')

