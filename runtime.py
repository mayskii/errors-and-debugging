def get_3rd_value(my_list):
    if len(my_list) > 2:
        return my_list[2]
    return None

def test_get_3rd_value():
    assert get_3rd_value([0, 1, 2]) == 2
    assert get_3rd_value([0, 1]) == None

def get_last_value(my_list):
    if len(my_list) == 0:
        return None
    return my_list[len(my_list) - 1]

def test_get_last_value():
    assert get_last_value([0, 1, 2]) == 2
    assert get_last_value([0]) == 0
    assert get_last_value([]) == None

def runtime_errors():
    test_get_3rd_value()
    test_get_last_value()

