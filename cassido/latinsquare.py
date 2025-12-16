#!/usr/bin/env python3
"""This week's (2025-12-15) question:Write a function to generate a Latin Square given a positive integer n. 
The values can be any n distinct values, and don't have to be consistent for different n."""
def latinSquare(n):
    """Generate an n x n Latin Square using numbers 1 to n."""
    square = []
    for i in range(n):
        row = [(j + i) % n + 1 for j in range(n)]
        square.append(row)
    return square

if __name__ == "__main__":
    print(latinSquare(1))
    print(latinSquare(2))
    print(latinSquare(4))
