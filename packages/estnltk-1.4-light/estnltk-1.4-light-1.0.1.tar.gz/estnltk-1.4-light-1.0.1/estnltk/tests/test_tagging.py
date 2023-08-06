# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

import unittest
from ..text import Text
from ..names import *


class TaggingTest(unittest.TestCase):

    def test_tagging(self):
        text = Text('Natukene teksti')

        self.assertFalse(text.is_tagged(PARAGRAPHS))
        self.assertFalse(text.is_tagged(SENTENCES))
        self.assertFalse(text.is_tagged(WORDS))
        self.assertFalse(text.is_tagged(ANALYSIS))

        text.tokenize_paragraphs()

        self.assertTrue(text.is_tagged(PARAGRAPHS))
        self.assertFalse(text.is_tagged(SENTENCES))
        self.assertFalse(text.is_tagged(WORDS))
        self.assertFalse(text.is_tagged(ANALYSIS))

        text.tokenize_sentences()

        self.assertTrue(text.is_tagged(PARAGRAPHS))
        self.assertTrue(text.is_tagged(SENTENCES))
        self.assertFalse(text.is_tagged(WORDS))
        self.assertFalse(text.is_tagged(ANALYSIS))

        text.tokenize_words()

        self.assertTrue(text.is_tagged(PARAGRAPHS))
        self.assertTrue(text.is_tagged(SENTENCES))
        self.assertTrue(text.is_tagged(WORDS))
        self.assertFalse(text.is_tagged(ANALYSIS))

        text.tag_analysis()

        self.assertTrue(text.is_tagged(PARAGRAPHS))
        self.assertTrue(text.is_tagged(SENTENCES))
        self.assertTrue(text.is_tagged(WORDS))
        self.assertTrue(text.is_tagged(ANALYSIS))
