"""
bite_279_armstrong_numbers
Created January 31, 2022 by Jennifer Baughman

Description: In number theory there are many interesting numbers - eg.
Armstrong numbers, Happy numbers, Meertens numbers, just to name a few.

In this bite, you will try to solve the Armstrong number question: given an
integer, determine if it is an armstrong number.

An armstrong number is a number that is the sum of its own digits each raised
to the power of the number of digits. See this reference for more info and
here are some examples:

a) 153 is an armstrong number. It's a 3 digits number:

    (1^3) + (5^3) + (3^3)= 153.
b) 371 is also an armstrong number.

c) any single digit numbers (1-9) are armstrong numbers as well.
"""


def is_armstrong(num):
    # checks for single digit number
    if num % 10 == num:
        return True
    digits = []
    n = num
    while n > 0:
        digits.insert(0, n % 10)
        n = n//10
    power = len(digits)
    return num == sum([x**power for x in digits])


def main():
    is_armstrong(1234)


if __name__ == "__main__":
    main()
