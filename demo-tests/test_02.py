import time 
import random

def test_func_02(load_review_rating):
    ## setup ##
    data, expected = load_review_rating

    ## call test fuction ##
    actual = int(data[:-1])
    time.sleep(abs(random.random()-0.5))

    ## assertion ##
    assert  actual > expected