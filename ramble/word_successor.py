
from enum import Enum, auto
from random import choice
from collections.abc import Callable


WordRule = Callable[[str, str], int]


class SuccessionMethod(Enum):
    '''Allowed succesion methods for WordSuccessor
    '''
    RANDOM = auto()
    FIRST = auto()
    MANUAL = auto()


def find_matching_words(
    word: str,
    rule: WordRule,
    vocabulary: set[str]
) -> list[str]:
    '''Find all words from vocabulary that matches with word.

    Args:
        word (str): The word to be matched.
        rule (WordRule): The rule used to match word.
        vocabulary (set[str]): A set of words.

    Returns:
        list[str]: All words matching the given word using the given word rule.
    '''
    return [w for w in vocabulary if rule(word, w)]


def choose_word(
    words: list[str],
    method: SuccessionMethod = SuccessionMethod.RANDOM
) -> str:
    '''Chose word from a list of words.

    Args:
        words (list[str]): List of strings to chose from.
        method (SuccessionMethod, optional): Method to use for the choice.
            Defaults to SuccessionMethod.RANDOM.

    Raises:
        IndexError: If list is empty.

    Returns:
        str: A word from the list.
    '''
    if not words:
        raise IndexError('No words to chose from.')
    if not isinstance(method, SuccessionMethod):
        raise TypeError('Method must be of type SuccesionMethod')
    if method == SuccessionMethod.RANDOM:
        # Pick a random word
        return choice(words)
    if method == SuccessionMethod.FIRST:
        # Pick the first word
        return words[0]
    if method == SuccessionMethod.MANUAL:
        # TODO: implement
        pass
    raise ValueError(f'Unrecognized method: {method}')


class WordSuccessor:
    '''WordSuccessor class to generate new words from a initial word.
    '''

    def __init__(
            self,
            initial_word: str,
            rule: WordRule,
            vocabulary: set[str],
            succession_method: SuccessionMethod = SuccessionMethod.RANDOM,
    ):
        self.current_word = initial_word
        self.rule = rule
        self.vocabulary = vocabulary
        self.succession_method = succession_method

    def __iter__(self):
        return self

    def __next__(self) -> str:
        '''Returns the next word
        '''
        matches = find_matching_words(
            self.current_word, self.rule, self.vocabulary
        )
        if not matches:
            raise StopIteration
        self.current_word = choose_word(
            matches,
            self.succession_method
        )
        return self.current_word
