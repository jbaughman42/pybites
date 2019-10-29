"""
bite_101_fstrings
Created October 29, 2019 by Jennifer Baughman

Description:
"""

MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    if age < MIN_DRIVING_AGE:
        print(f"{name} is not allowed to drive")
    else:
        print(f"{name} is allowed to drive")
