import random 
import pytest
import pandas as pd

data_path = "pytest-demo/resources/genres_and_15_best_of_films.csv"
data = pd.read_csv(data_path)
data = [data.iloc[idx] for idx in range(len(data))]

@pytest.fixture(params=random.sample(data, 20))
def load_review_rating(request):
    return request.param["review_rating"], 80

@pytest.fixture(params=[1,2,3,4,5])
def load_number(request):
    return request.param

@pytest.fixture(scope="module")
def get_connection():
    connection = mongo.connect()
    return connection

@pytest.fixture()
def df():
    return pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
    })


@pytest.fixture()
def df_with_col_d():
    return pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
        'col_d': ['d', 'd', 'd'],
    })