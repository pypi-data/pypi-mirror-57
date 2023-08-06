# -*- coding: utf-8 -*-
"""Module that defines the attribute names and constants used througout the library
and in corpora."""

from __future__ import unicode_literals, print_function, absolute_import

# commonly required attributes
START = 'start'
END = 'end'
REL_START = 'rel_start'
REL_END = 'rel_end'
TEXT = 'text'

# document-level attributes
WORDS = 'words'
SENTENCES = 'sentences'
PARAGRAPHS = 'paragraphs'
DOCUMENTS = 'documents'
FILE = 'file'  # the file path of the source corpus

# word attributes
ANALYSIS = 'analysis'
LEMMA = 'lemma'
POSTAG = 'partofspeech'
ROOT = 'root'
ROOT_TOKENS = 'root_tokens'
CLITIC = 'clitic'
ENDING = 'ending'
FORM = 'form'
SPELLING = 'spelling'
SUGGESTIONS = 'suggestions'
GT_WORDS = 'gt_words'  # words and morph analyses in gt format;
