from typing import Callable


WordRule = Callable[[str, str], int]


def matching_suffix(w1: str, w2: str) -> int:
    if w1 == w2:
        return 0
    idx = 1
    while w1[-idx:] == w2[-idx:]:
        idx += 1
    return idx - 1


def alphabet_rule(alphabet: set) -> WordRule:
    '''Returns a word rule which only allows letters from specified alphabet.

    Args:
        alphabet (set): The set of allowed letters
    '''
    def rule(_, w2):
        return int(set(letter for letter in w2).issubset(alphabet))
    return rule
