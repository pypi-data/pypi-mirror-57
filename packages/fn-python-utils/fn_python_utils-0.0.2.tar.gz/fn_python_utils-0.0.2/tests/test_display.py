# -*- coding: utf-8 -*-

import pytest

import fn_python_utils.display as display_m



def create_input(N, gen=False):
    result = ("elt_n°{}".format(i) for i in range(N))
    if not gen:
        result = list(result)
    return result

def create_test_function(list_to_test, id_):
    def func_(string):
        list_to_test.append(string)
    func_.__name__ = "func_id={}".format(id_)
    return func_


def get__create_threshold_count2percentage_data_test_data():
    test_data = []
    ids = []
    
    #
    maximum_count = 100
    percentage_interval = 5
    expected_result = {
        0: (0, 0, 100),
        5: (5, 5, 100),
        10: (10, 10, 100),
        15: (15, 15, 100),
        20: (20, 20, 100),
        25: (25, 25, 100),
        30: (30, 30, 100),
        35: (35, 35, 100),
        40: (40, 40, 100),
        45: (45, 45, 100),
        50: (50, 50, 100),
        55: (55, 55, 100),
        60: (60, 60, 100),
        65: (65, 65, 100),
        70: (70, 70, 100),
        75: (75, 75, 100),
        80: (80, 80, 100),
        85: (85, 85, 100),
        90: (90, 90, 100),
        95: (95, 95, 100),
        100: (100, 100, 100),
        }
    
    args = (percentage_interval, maximum_count,)
    kwargs = {}
    test_datum = (args, kwargs, expected_result)
    id_ = "100_5%"
    test_data.append(test_datum)
    ids.append(id_)
    
    #
    maximum_count = 10
    percentage_interval = 5
    expected_result = {
        0: (0, 0, 10),
        1: (10, 1, 10),
        2: (20, 2, 10),
        3: (30, 3, 10),
        4: (40, 4, 10),
        5: (50, 5, 10),
        6: (60, 6, 10),
        7: (70, 7, 10),
        8: (80, 8, 10),
        9: (90, 9, 10),
        10: (100, 10, 10),
        }
    
    args = (percentage_interval, maximum_count,)
    kwargs = {}
    test_datum = (args, kwargs, expected_result)
    id_ = "10_5%"
    test_data.append(test_datum)
    ids.append(id_)
    
    #
    maximum_count = 10
    percentage_interval = 7
    expected_result = {
        0: (0, 0, 10),
        1: (7, 1, 10),
        2: (14, 2, 10),
        3: (28, 3, 10),
        4: (35, 4, 10),
        5: (49, 5, 10),
        6: (56, 6, 10),
        7: (70, 7, 10),
        8: (77, 8, 10),
        9: (84, 9, 10),
        10: (98, 10, 10)
        }
    
    args = (percentage_interval, maximum_count,)
    kwargs = {}
    test_datum = (args, kwargs, expected_result)
    id_ = "10_7%"
    test_data.append(test_datum)
    ids.append(id_)
    
    return {"params": test_data, "ids": ids}
@pytest.fixture(**get__create_threshold_count2percentage_data_test_data())
def one_input__create_threshold_count2percentage_data_test_data_fixture(request):
    return request.param


def get_create_display_progress_function_test_data():
    test_data = []
    ids = []
    
    #
    maximum_count = 100
    percentage_interval = 5
    count_interval = 1000
    personalized_progress_message = "{percentage:6.2f}; {current:d}; {total:d}"
    input_expected_result_pairs = [
        (0, "  0.00; 0; 100"),
        (2, None),
        (5, "  5.00; 5; 100"),
        (10, " 10.00; 10; 100"),
        (65, " 65.00; 65; 100"),
        (59, None),
        (100, "100.00; 100; 100"),
        ]
    id_ = "per_5%"
    function_content = []
    test_func = create_test_function(function_content, id_)
    
    args = (test_func,)
    kwargs = {"maximum_count": maximum_count, 
              "percentage_interval": percentage_interval, 
              "count_interval": count_interval, 
              "personalized_progress_message": personalized_progress_message,
              }
    test_datum = ((args, kwargs), (function_content, input_expected_result_pairs))
    test_data.append(test_datum)
    ids.append(id_)
    
    #
    maximum_count = 10
    percentage_interval = 5
    count_interval = 1000
    personalized_progress_message = "{percentage:6.2f}; {current:d}; {total:d}"
    input_expected_result_pairs = [
        (0, "  0.00; 0; 10"),
        (2, " 20.00; 2; 10"),
        (7, " 70.00; 7; 10"),
        (1, " 10.00; 1; 10"),
        (49, None),
        (10, "100.00; 10; 10"),
        ]
    id_ = "per_5%_small"
    function_content = []
    test_func = create_test_function(function_content, id_)
    
    args = (test_func,)
    kwargs = {"maximum_count": maximum_count, 
              "percentage_interval": percentage_interval, 
              "count_interval": count_interval, 
              "personalized_progress_message": personalized_progress_message,
              }
    test_datum = ((args, kwargs), (function_content, input_expected_result_pairs))
    test_data.append(test_datum)
    ids.append(id_)
    
    #
    maximum_count = 10
    percentage_interval = 7
    count_interval = 1000
    personalized_progress_message = "{percentage:6.2f}; {current:d}; {total:d}"
    input_expected_result_pairs = [
        (0, "  0.00; 0; 10"),
        (2, " 14.00; 2; 10"), # FIXME: to correct should be 21
        (7, " 70.00; 7; 10"),
        (1, "  7.00; 1; 10"),
        (49, None),
        (10, " 98.00; 10; 10"),
        ]
    id_ = "per_7_small%"
    function_content = []
    test_func = create_test_function(function_content, id_)
    
    args = (test_func,)
    kwargs = {"maximum_count": maximum_count, 
              "percentage_interval": percentage_interval, 
              "count_interval": count_interval, 
              "personalized_progress_message": personalized_progress_message,
              }
    test_datum = ((args, kwargs), (function_content, input_expected_result_pairs))
    test_data.append(test_datum)
    ids.append(id_)
    
    #
    maximum_count = None
    percentage_interval = 5
    count_interval = 10
    personalized_progress_message = None
    input_expected_result_pairs = [
        (0, "Iteration n°0"),
        (2, None),
        (5, None),
        (10, "Iteration n°10"),
        (65, None),
        (59, None),
        (30, "Iteration n°30"),
        (100, "Iteration n°100"),
        ]
    id_ = "per_10_it"
    function_content = []
    test_func = create_test_function(function_content, id_)
    
    args = (test_func,)
    kwargs = {"maximum_count": maximum_count, 
              "percentage_interval": percentage_interval, 
              "count_interval": count_interval, 
              "personalized_progress_message": personalized_progress_message,
              }
    test_datum = ((args, kwargs), (function_content, input_expected_result_pairs))
    test_data.append(test_datum)
    ids.append(id_)
    
    return {"params": test_data, "ids": ids}
@pytest.fixture(**get_create_display_progress_function_test_data())
def one_input_create_display_progress_function_test_data_fixture(request):
    return request.param



def get_create_logged_iterator_wrapper_test_data():
    test_data = []
    ids = []
    
    #
    percentage_interval = 5
    count_interval = 1000
    personalized_progress_message = "{percentage:6.2f}; {current:d}; {total:d}"
    N = 200
    iterator = create_input(N, gen=False)
    id_ = "Len_N=200"
    actual_result = []
    test_func = create_test_function(actual_result, id_)
    expected_result = [
        "  0.00; 0; 200",
        "  5.00; 10; 200",
        " 10.00; 20; 200",
        " 15.00; 30; 200",
        " 20.00; 40; 200",
        " 25.00; 50; 200",
        " 30.00; 60; 200",
        " 35.00; 70; 200",
        " 40.00; 80; 200",
        " 45.00; 90; 200",
        " 50.00; 100; 200",
        " 55.00; 110; 200",
        " 60.00; 120; 200",
        " 65.00; 130; 200",
        " 70.00; 140; 200",
        " 75.00; 150; 200",
        " 80.00; 160; 200",
        " 85.00; 170; 200",
        " 90.00; 180; 200",
        " 95.00; 190; 200",
        ]
    
    args = (test_func,)
    kwargs = {"percentage_interval": percentage_interval, 
              "count_interval": count_interval, 
              "personalized_progress_message": personalized_progress_message,
              }
    test_datum = (args, kwargs, iterator, actual_result, expected_result)
    test_data.append(test_datum)
    ids.append(id_)
    
    return {"params": test_data, "ids": ids}
@pytest.fixture(**get_create_logged_iterator_wrapper_test_data())
def one_input_create_logged_iterator_wrapper_test_data_fixture(request):
    return request.param



class Test(object):
    
    def test__create_threshold_count2percentage_data(self, one_input__create_threshold_count2percentage_data_test_data_fixture):
        # Test parameter
        args, kwargs, expected_result = one_input__create_threshold_count2percentage_data_test_data_fixture
        
        # Test
        actual_result = display_m._create_threshold_count2percentage_data(*args, **kwargs)
        assert expected_result == actual_result
    
    def test_create_display_progress_function(self, one_input_create_display_progress_function_test_data_fixture):
        # Test parameters
        (args, kwargs), (function_content, input_expected_result_pairs) = one_input_create_display_progress_function_test_data_fixture
        
        # Test
        display_function = display_m.create_display_progress_function(*args, **kwargs)
        
        actual_results = []
        expected_results = []
        current_function_content_length = len(function_content)
        for input_, expected_result in input_expected_result_pairs:
            expected_results.append(expected_result)
            display_function(input_)
            if current_function_content_length < len(function_content):
                actual_results.extend(function_content[current_function_content_length:])
                current_function_content_length = len(function_content)
            else:
                actual_results.append(None)
            
        assert expected_results == actual_results
    
    def test_create_logged_iterator_wrapper(self, one_input_create_logged_iterator_wrapper_test_data_fixture):
        # Test parameters
        args, kwargs, iterator, actual_result, expected_result = one_input_create_logged_iterator_wrapper_test_data_fixture
        
        # Test
        wrapper_function = display_m.create_logged_iterator_wrapper(*args, **kwargs)
        assert len(actual_result) == 0
        wrapped_iterator = wrapper_function(iterator)
        tuple(wrapped_iterator)
        assert expected_result == actual_result

