"""
sum_n_numbers
Created January 27, 2022 by Jennifer Baughman

Description: Write a Python function that calculates the sum of a list of
numbers:

The function should accept a list of numbers and return the sum of those
numbers.
If no argument is provided (that is, numbers is None), return the sum of the
numbers 1 to 100 (Note that this is not the same as an empty list of numbers
being passed in. In that case the sum returned will be 0).
"""


def sum_n_numbers(nums):
    if nums is None:
        nums = range(1, 101)
    return sum(nums)


def main():
    nums = [5, 10, 2, 14, 67]
    print(sum_n_numbers([]))


if __name__ == "__main__":
    main()
