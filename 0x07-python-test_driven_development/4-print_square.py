#!/usr/bin/python3
"""
This module provides a function for printing a square using the char '#'.
"""


def print_square(size):
    """
    Prints a square using the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If `size` is not an integer or is a float.
        ValueError: If `size` is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is >= 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
