'''Test word_successor.
'''
from typing import Iterable, Type
import unittest

from ramble import choose_word, find_matching_words
from ramble.word_successor import WordSuccessor, SuccessionMethod
from ramble.word_rules import alphabet_rule, matching_suffix


class WordSuccessorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.init_word = 'vandmelon'
        self.method = SuccessionMethod.FIRST
        self.word_list = ['abe', 'kanon', 'trold']
        self.vocabulary = {
            'atavistisk', 'ateisme', 'ateist', 'ateistisk',
            'atelier', 'ateliervindue', 'Athen', 'athener', 'athenienser',
            'atheniensisk', 'athensk', 'Atlanten', 'Atlanterhavet', 'atlantisk',
            'atlas', 'atlask', 'atlaskeskjole', 'atlet', 'atletik', 'atletisk'
        }
        self.vocabulary_small = {'abc', 'bacd', 'cd', 'xyz', 'axc', 'xcd'}

        # rules
        self.alph_rule = alphabet_rule({'a', 'b', 'c', 'd'})
        self.sufx_rule = matching_suffix

    def test_choose_word(self) -> None:
        ''' Tests the choose_word function.
        '''
        first_word = choose_word(self.word_list, SuccessionMethod.FIRST)
        self.assertEqual(first_word, 'abe')
        self.assertRaises(IndexError, choose_word, [], self.method)
        self.assertRaises(TypeError, choose_word, self.word_list, 'MY_METHOD')
        results = set()
        for _ in range(1000):
            results.add(choose_word(self.word_list, SuccessionMethod.RANDOM))
        self.assertEqual(len(results), 3)

    def test_find_matching_words(self):

        self.assertEquals(
            set(find_matching_words('a', self.alph_rule, self.vocabulary_small)),
            {'abc', 'bacd', 'cd'}
        )

        self.assertEquals(
            set(find_matching_words('cd', self.sufx_rule, self.vocabulary_small)),
            {'bacd', 'xcd'}
        )
        self.assertEquals(
            find_matching_words('stk', self.sufx_rule, self.vocabulary_small),
            []
        )
        self.assertNotIn(
            'cd',
            find_matching_words('cd', self.sufx_rule, self.vocabulary_small)
        )

    def test_next(self):
        vocab = {'abc', 'xbc', 'cba'}
        ws = WordSuccessor(
            'abc',
            rule=self.sufx_rule,
            vocabulary=vocab,
            succession_method=SuccessionMethod.FIRST
        )
        self.assertEquals(next(ws), 'xbc')
        self.assertEquals(next(ws), 'abc')
        self.assertEquals(next(ws), 'xbc')

        ws = WordSuccessor(
            'cba',
            rule=self.sufx_rule,
            vocabulary=vocab,
            succession_method=SuccessionMethod.FIRST
        )
        self.assertRaises(StopIteration, next, ws)
        self.assertIsInstance(ws, Iterable)


if __name__ == '__main__':
    unittest.main()
