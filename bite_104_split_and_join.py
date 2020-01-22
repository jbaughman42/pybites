"""
bite_104_split_and_join
Created January 22, 2020 by Jennifer Baughman

Description:
"""

message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    return "|".join(message.split("\n"))


def main():
    print(split_in_columns(message))


if __name__ == "__main__":
    main()
