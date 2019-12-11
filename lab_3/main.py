"""
Labour work #3
 Building an own N-gram model
"""

import math


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

    def get_original_by(self, idd: int) -> str:
        if isinstance(idd, int) and idd in self.storage.values():
            for word, i in self.storage.items():
                if i == idd:
                    return word
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple):
            for word in corpus:
                self.put(word)
            return self.storage
        return {}


class NGramTrie:
    def __init__(self, n=2):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        gram = []
        if isinstance(sentence, tuple) and sentence is not None and len(sentence) > self.size:
            for ind, _ in enumerate(sentence[:-self.size + 1]):
                gram = []
                i = 0
                while i < self.size:
                    gram.append(sentence[ind + i])
                    i += 1
                gram = tuple(gram)
                if gram in self.gram_frequencies:
                    self.gram_frequencies[gram] += 1
                else:
                    self.gram_frequencies[gram] = 1
            if not gram:
                return "ERROR"
            return "OK"
        else:
            return "ERROR"

    def calculate_log_probabilities(self):
        prefixes = {}
        for gram in self.gram_frequencies:
            pref = gram[:-1]
            if pref in prefixes:
                prefixes[pref] += self.gram_frequencies[gram]
            else:
                prefixes[pref] = self.gram_frequencies[gram]
        for gram in self.gram_frequencies:
            if gram not in list(self.gram_log_probabilities):
                self.gram_log_probabilities[gram] = math.log(self.gram_frequencies[gram]/prefixes[gram[:-1]])

    def predict_next_sentence(self, prefix: tuple) -> list:
        if prefix is None or not isinstance(prefix, tuple) or len(prefix) + 1 != self.size:
            return []
        list_of_keys = list(self.gram_log_probabilities.keys())
        new_sentence = list(prefix)
        while True:
            new_list = []
            for gram in list_of_keys:
                if gram[:-1] == prefix:
                    new_list.append(self.gram_log_probabilities[gram])
            if not new_list:
                break
            new_word = max(new_list)
            for word, probability in list(self.gram_log_probabilities.items()):
                if new_word == probability:
                    new_word = word[-1]
            new_sentence.append(new_word)
            new_prefix = list(prefix[1:])
            new_prefix.append(new_word)
            prefix = tuple(new_prefix)
        return new_sentence


def encode(storage_instance, corpus) -> list:
    coded = []
    for _ in corpus:
        for_coded = []
        for word in _:
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
        sentences_1 = []
        corpus = []
        for symbol in text:
            s = text[text.index(symbol) - 2]
            if symbol.isalpha() or symbol == ' ':
                if symbol.isupper() and s == '.':
                    symbol = 'sep'+symbol
                new_text += symbol.lower()
            sentences_1 = new_text.split('sep')
        while '' in sentences_1:
            sentences_1.remove('')
        for i in sentences_1:
            i = i.split()
            i.insert(0, '<s>')
            i.append('</s>')
            corpus.append(i)
        return list(corpus)
    return []


WSt = WordStorage()
NGr = NGramTrie(2)
sentences = split_by_sentence(REFERENCE_TEXT)
for sent in sentences:
    for word_ in sent:
        WSt.put(word_)
sentences1 = encode(WSt, sentences)
for sent in sentences1:
    NGr.fill_from_sentence(tuple(sent))
NGr.calculate_log_probabilities()
prefix1 = 'she'
pref_lst = prefix1.split()
pref_num = []
for pref in pref_lst:
    pref_num.append(WSt.get_id_of(pref))
numbers_res = NGr.predict_next_sentence(tuple(pref_num))
fin = []
for number in numbers_res:
    fin.append(WSt.get_original_by(number))
print(fin)



#  id_of_word = WS.get_id_of(word_train)
# final = NGR.predict_next_sentence(tuple(id_of_word) )
#  print(final)






