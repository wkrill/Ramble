'''Test word_rules.
'''
import unittest
from typing import Type

from ramble.word_rules import WordRule
from ramble.word_rules import alphabet_rule
from ramble.word_rules import matching_suffix


class WordSuccessorTests(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_matching_suffix(self) -> None:
        ''' Tests the matching_suffix rule.
        '''
        self.assertNotEquals(matching_suffix('abe', 'giraf'), 0)
        self.assertEquals(matching_suffix('abe', 'skole'), 1)
        self.assertEquals(matching_suffix('telegraf', 'giraf'), 3)
        self.assertEquals(matching_suffix('telegraf', 'telegraf'), 0)

    def test_alphabet_rule(self) -> None:
        a = set(letter for letter in 'abcdefghi')
        x = {'x', 'y', 'z'}
        rule_a = alphabet_rule(alphabet=a)
        rule_x = alphabet_rule(alphabet=x)

        self.assertEquals(rule_a('abc', 'abcdba'), 1)
        self.assertEquals(rule_x('abc', 'abcdba'), 0)
        self.assertEquals(rule_a('abc', 'abcxdba'), 0)
        self.assertEquals(rule_a('abc', 'abcxdba'), 0)
        # First word does not matter
        self.assertEquals(rule_a('xyz', 'abcdba'), 1)
        self.assertEquals(rule_x('xyz', 'abcdba'), 0)
        self.assertEquals(rule_x('askdja', 'xzxxyz'), 1)


if __name__ == '__main__':
    unittest.main()
