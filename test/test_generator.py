import unittest
from generator import generator

def test_sample_single_word():
    l = ('test', 'a', 'word')
    word = generator.sample(l)
    assert word in l

def test_sample_multiple_words():
    l = ('test', 'multiple', 'words')
    words = generator.sample(l, 2)
    assert len(words) == 2


def test_generate_a_movie_with_tree_words():
    movie = generator.generate_movie()
    assert len(movie.split(' ')) >= 3