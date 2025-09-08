def count_positive_numbers(nums):
    count = 0
    for num in nums:
        if num > 0:
            count += 1

    return count

def test_count_positive_numbers():
    assert count_positive_numbers([-2, -1, 0, 1, 2]) == 2
    assert count_positive_numbers([-2, -1]) == 0

def logical_errors():
    test_count_positive_numbers()