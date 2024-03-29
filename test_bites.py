import pytest

import bite_1_sum_n_numbers as sum_n
from bite_279_armstrong_numbers import is_armstrong
from bite_2_regex_fun import (extract_course_times,
                              get_all_hashtags_and_links,
                              match_first_paragraph)
from bite_3_word_values import calc_word_value, load_words, max_word_value
from bite_5_parse_name_list import (NAMES, dedup_and_title_case_names,
                                    shortest_first_name, sort_by_surname_desc)
from bite_9_palindromes import (get_longest_palindrome, is_palindrome,
                                load_dictionary)
from test_bites_data import *


@pytest.mark.skip
def test_sum_n_numbers():
    assert sum_n.sum_n_numbers([1, 2, 3, 4, 5]) == 15


@pytest.mark.skip
def test_sum_n_numbers_none():
    assert sum_n.sum_n_numbers(None) == 5050


@pytest.mark.skip
def test_sum_n_numbers_empty():
    assert sum_n.sum_n_numbers([]) == 0


@pytest.mark.skip
def test_extract_course_times_default_arg():
    expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
    assert extract_course_times() == expected


@pytest.mark.skip
def test_extract_course_times_other_course_input():
    course = ('00:40 Lesson introduction'
              '01:33 Your 3 day overview'
              '08:12 Learning datetime and date'
              '06:07 Datetime timedelta usage'
              '04:02 Concepts: what did we learn')
    expected = ['00:40', '01:33', '08:12', '06:07', '04:02']
    assert extract_course_times(course) == expected


@pytest.mark.skip
def test_get_all_hashtags_and_links_default_arg():
    expected = ['http://pybit.es/requests-cache.html', '#python', '#APIs']
    assert get_all_hashtags_and_links() == expected


@pytest.mark.skip
def test_get_all_hashtags_and_links_other_tweet():
    tweet = ('PyBites My Reading List | 12 Rules for Life - #books '
             'that expand the mind! '
             'http://pbreadinglist.herokuapp.com/books/'
             'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'
             ' #psychology #philosophy')
    expected = ['#books',
                ('http://pbreadinglist.herokuapp.com/books/'
                 'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'),
                '#psychology', '#philosophy']
    assert get_all_hashtags_and_links(tweet) == expected


@pytest.mark.skip
def test_match_first_paragraph_default_arg():
    expected = 'pybites != greedy'
    assert match_first_paragraph() == expected


words = load_words()


@pytest.mark.skip
def test_load_words():
    assert type(words) == list
    assert len(words) == 235886
    assert words[0] == 'A'
    assert words[-1] == 'Zyzzogeton'
    assert ' ' not in ''.join(words)


@pytest.mark.skip
def test_calc_word_value():
    assert calc_word_value('bob') == 7
    assert calc_word_value('JuliaN') == 13
    assert calc_word_value('PyBites') == 14
    assert calc_word_value('benzalphenylhydrazone') == 56


@pytest.mark.skip
def test_max_word_value():
    test_words = ['bob', 'julian', 'pybites', 'quit', 'barbeque']
    assert max_word_value(test_words) == 'barbeque'
    assert max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'


@pytest.mark.skip
def test_non_scrabble_characters():
    # thanks Joakim
    assert max_word_value(["a", "åäö"]) == "a"


@pytest.mark.skip
def test_dedup_and_title_case_names():
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Bob Belderbos') == 1
    assert names.count('julian sequeira') == 0
    assert names.count('Brad Pitt') == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)


@pytest.mark.skip
def test_dedup_and_title_case_names_different_names_list():
    actual = sorted(dedup_and_title_case_names(PY_CONTENT_CREATORS))
    expected = ['Brian Okken', 'Dan Bader', 'Julian Sequeira',
                'Matt Harrison', 'Michael Kennedy', 'Trey Hunner']
    assert actual == expected


@pytest.mark.skip
def test_sort_by_surname_desc():
    names = sort_by_surname_desc(NAMES)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Alec Baldwin'


@pytest.mark.skip
def test_sort_by_surname_desc_different_names_list():
    names = sort_by_surname_desc(PY_CONTENT_CREATORS)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Dan Bader'


@pytest.mark.skip
def test_shortest_first_name():
    assert shortest_first_name(NAMES) == 'Al'


@pytest.mark.skip
def test_shortest_first_name_different_names_list():
    assert shortest_first_name(PY_CONTENT_CREATORS) == 'Dan'


@pytest.mark.skip
@pytest.mark.parametrize('number, expected', [
    (5, True), (153, True), (370, True),
    (371, True), (4150, False), (2020, False),
    (9474, True), (1989, False), (11, False),
])
def test_armstrong(number, expected):
    assert is_armstrong(number) == expected


@pytest.mark.skip
def test_is_palidrome():
    assert is_palindrome('Aibohphobia')
    assert is_palindrome('Avid diva')
    assert is_palindrome('Avid diva. ')
    assert is_palindrome('A Toyota’s a Toyota.')
    assert is_palindrome('A man, a plan, a canal: Panama')
    assert is_palindrome("No 'x' in 'Nixon'")
    assert is_palindrome('malayalam')
    
    assert not is_palindrome('PyBites')
    assert not is_palindrome('malayalan')
    assert not is_palindrome('toyota')
    assert not is_palindrome('palindrome')


@pytest.mark.skip
def test_get_longest_palindrome():
    words = load_dictionary()
    assert get_longest_palindrome() == 'malayalam'
    
    new_longest = 'A car, a man, a maraca.'
    words = list(words) + [new_longest]
    assert get_longest_palindrome(words) == new_longest
