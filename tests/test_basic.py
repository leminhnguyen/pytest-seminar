import pandas as pd

def add_col(df, new_col_name, default_value):
    """Add a new column to the given dataframe with a default value"""
    if new_col_name in df.columns:
        raise ValueError('column already exists')

    df[new_col_name] = default_value

    return df


def test_add_col_passes():
    # setup
    df = pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
    })

    # call function
    actual = add_col(df, 'col_d', 'd')

    # set expectations
    expected = pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
        'col_d': ['d', 'd', 'd'],
    })

    # assertion
    pd.testing.assert_frame_equal(actual, expected)


def test_add_col_passes_with_fixtures(df, df_with_col_d):
    actual = add_col(df, 'col_d', 'd')
    expected = df_with_col_d
    pd.testing.assert_frame_equal(actual, expected)