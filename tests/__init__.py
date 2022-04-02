'''Test suite.
'''
import unittest

from .test_word_successor import WordSuccessorTests  # noqa: F401


def main_tests() -> None:
    unittest.main()


if __name__ == "__main__":
    main_tests()
