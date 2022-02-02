"""
bite_9_palindromes
Created February 02, 2022 by Jennifer Baughman

Description: A palindrome is a word, phrase, number, or other sequence of
characters which reads the same backward as forward.

Write a function to determine if a word (or phrase) is a palindrome.

Then write a second function to receive a word (or phrase) list and determine
which word is the longest palindrome.

See the template code / docstrings below for further requirements as well as
the tests.
"""

import os
import string
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
        DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    
    # strip everything not a letter and convert to lowercase
    word = ''.join([l for l in word.lower() if l in string.ascii_lowercase])
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if not words:
        words = load_dictionary()
    pals = [word for word in words if is_palindrome(word)]
    return max(pals, key=len)

    


def main():
    get_longest_palindrome()


if __name__ == "__main__":
    main()
