#!/usr/bin/env python3
"""This week's (2025-11-17) question:
Given a positive integer n, write a function that returns an array containing all integers from 1 to n, where each integer i appears exactly i times in the result. For example, 3 should appear 3 times, 5 should appear 5 times, and so on. The order of the integers in the output array does not matter."""

def repeatedIntegers(n):
    result = []
    for i in range(1, n + 1):
        result.extend([i] * i)
    return result

if __name__ == "__main__":
    print(repeatedIntegers(4))
    