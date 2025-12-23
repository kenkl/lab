#!/usr/bin/env python3
"""This week's (2025-12-22) question:
An alternating array is a list of any length in which two (not necessarily different) values are alternating (all even-indexed items are equal, and all odd-indexed items are equal). Given an array, return true if it is alternating.

Examples:

[]             -> True
[1]            -> True
[1,1]          -> True
[1,2,1]        -> True
[10,5,10,5,10] -> True
[2,2,3,3]      -> False
[5,4,3,5,4,3]  -> False
"""
def is_alternating_array(arr):
    if len(arr) < 2:
        return True
    first_value = arr[0]
    second_value = arr[1]
    for i in range(len(arr)):
        if i % 2 == 0:
            if arr[i] != first_value:
                return False
        else:
            if arr[i] != second_value:
                return False
    return True

if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [],
        [1],
        [1, 1],
        [1, 2, 1],
        [10, 5, 10, 5, 10],
        [2, 2, 3, 3],
        [5, 4, 3, 5, 4, 3]
    ]
    for arr in test_arrays:
        print(f"{arr} -> {is_alternating_array(arr)}")
