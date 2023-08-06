""" Exploratory Data Analysis(EDA) for helping you check your data
"""

import pandas as pd
import webbrowser
import os


def create_data_for_test():
    """ create a pandas DataFrame for test
    """
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                       'b': [6, 7, 8, 9, 10],
                       'c': ['x', 'y', 'z', 'h', 'i']
                       }
                      )
    return df


def data_profiling(df):
    """v0.0.1 for test,later this will depre
    """
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file("datasets/df.html")


if __name__ == '__main__':
    df = create_data_for_test()
    data_profiling(df)
    webbrowser.open_new_tab('datasets/df.html')


