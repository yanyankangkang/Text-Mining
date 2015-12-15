__author__ = 'Hao'

import re


def contains_digit(word):
    return bool(re.search("[0-9]", word))


def is_2_digit_num(word):
    return len(word) == 2 and word.isdigit()


def is_4_digit_num(word):
    return len(word) == 4 and word.isdigit()


def is_other_num(word):
    return word.isdigit() and not is_2_digit_num(word) and not is_4_digit_num(word)


def contains_digit_and_alpha(word):
    return bool(re.search("[a-zA-Z]", word)) and contains_digit(word)


def contains_digit_and_dash(word):
    return "-" in word and contains_digit(word)


def contains_digit_and_slash(word):
    return "/" in word and contains_digit(word)


def contains_digit_and_comma(word):
    return "," in word and contains_digit(word)


def contains_digit_and_period(word):
    return "." in word and contains_digit(word)


def is_all_caps(word):
    return re.match("^[A-Z]+$", word)


def is_lowercase(word):
    return re.match("^[a-z]+$", word)


def is_init_cap(word):
    return len(word) > 0 and word[0].isupper() and word[1:].islower()


def is_city_name(word):
        return word in CITIES


def get_cities(file_name):
    cities = set()
    with open(file_name) as f:
        cities.update(f.read().splitlines())
    return cities

CITIES = get_cities("cities.txt")
FEATURE_TABLE = dict()
FEATURE_TABLE[is_2_digit_num] = "1"  # TwoDigitNum
FEATURE_TABLE[is_4_digit_num] = "2"  # FourDigitNum
FEATURE_TABLE[is_other_num] = "3"  # OtherNum
FEATURE_TABLE[contains_digit_and_alpha] = "4"  # ContainsDigitAndAlpha
FEATURE_TABLE[contains_digit_and_dash] = "5"  # ContainsDigitAndDash
FEATURE_TABLE[contains_digit_and_slash] = "6"  # ContainsDigitAndSlash
FEATURE_TABLE[contains_digit_and_comma] = "7"  # ContainsDigitAndComma
FEATURE_TABLE[contains_digit_and_period] = "8"  # ContainsDigitAndPeriod
FEATURE_TABLE[is_all_caps] = "9"  # contains_digit_and_period
FEATURE_TABLE[is_lowercase] = "10"  # LowerCase
FEATURE_TABLE[is_init_cap] = "11"  # InitCap
FEATURE_TABLE[is_city_name] = "12"  # City