import time 
import random

def test_func_01(load_review_rating):
    ## setup ##
    data, expected = load_review_rating

    ## call test fuction ##
    actual = int(data[:-1])
    time.sleep(abs(random.random()-0.5))

    ## assertion ##
    assert  actual > expected

def test_query_1(get_connection):
    connection = get_connection
    connection.query()


def test_query_2(get_connection):
    connection = get_connection
    connection.query()