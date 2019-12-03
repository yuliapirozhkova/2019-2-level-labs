"""
Labour work #3
 Building an own N-gram model
"""

import math
from random import randint

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if isinstance(word, str) and word not in self.storage:
            word_id = len(self.storage)
            self.storage[word] = word_id
            return word_id
        return -1

    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage.get(word)
        return -1

    def get_original_by(self, id: int) -> str:
        if isinstance(id, int):
            for word, i in self.storage.items():
                if i == id:
                    return word
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple):
            for word in corpus:
                self.put(word)
            return self.storage
        return {}


class NGramTrie:
    def __init__(self, number=2):
        self.size = number
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.code = []

    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    coded = []
    for sentence in corpus:
        for_coded = []
        for word in sentence:
            word = storage_instance.get_id_of(word)
            for_coded.append(word)
        coded.append(coded)
    return coded


def split_by_sentence(text: str) -> list:
    if isinstance(text, str) and text is not '' and len(text) > 1 and len(text.split(' ')) > 1 and text is not None:
        new_text = ''
        text = text.replace('\n', '')
        text = text.replace('  ', ' ')
        text = text.replace('!', '.')
        text = text.replace('?', '.')
        text = text.replace('...', '.')
        sentences = []
        corpus = []
        for symbol in text:
            s = text[text.index(symbol) - 2]
            if symbol.isalpha() or symbol == ' ':
                if symbol.isupper() and s == '.':
                    symbol = 'sep'+symbol
                new_text += symbol.lower()
            sentences = new_text.split('sep')
        while '' in sentences:
            sentences.remove('')
        for i in sentences:
            i = i.split()
            i.insert(0, '<s>')
            i.append('</s>')
            corpus.append(i)
        return list(corpus)
    return []
