from math import log


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    corpus = []
    try:
        for one_text in texts:
            if not isinstance(one_text, str):
                continue
            one_text = one_text.lower()
            one_text = one_text.replace('\n', ' ')
            one_text = one_text.replace('<br />', ' ')
            for sign in one_text:
                if not sign.isalpha() and sign != ' ':
                    one_text = one_text.replace(sign, '')
            corpus.append(one_text.split())
        return corpus
    except TypeError:
        return []


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        try:
            for part in self.corpus:
                if not isinstance(part, list):
                    continue
                dict_for_part = {}
                new_part = []
                for element in part:
                    if isinstance(element, str):
                        new_part.append(element)
                for word in new_part:
                    if word not in dict_for_part:
                        dict_for_part[word] = part.count(word) / len(new_part)
                if dict_for_part:
                    self.tf_values.append(dict_for_part)
        except TypeError:
            return []

    def calculate_idf(self):
        try:
            length_corp = len(self.corpus)
            for element in self.corpus:
                if not isinstance(element, list):
                    length_corp -= 1
            for text_1 in self.corpus:
                if not isinstance(text_1, list):
                    continue
                for word in text_1:
                    if not isinstance(word, str):
                        continue
                    if word in self.idf_values:
                        continue
                    counter = 0
                    for element in self.corpus:
                        if not isinstance(element, list):
                            continue
                        if word in element:
                            counter += 1
                    self.idf_values[word] = log(length_corp / counter)
        except TypeError:
            return {}

    def calculate(self):
        try:
            for element in self.tf_values:
                temp_dict = {}
                for word, value in element.items():
                    temp_dict[word] = value * self.idf_values[word]
                self.tf_idf_values.append(temp_dict)
        except(KeyError, TypeError):
            return []

    def report_on(self, word, document_index):
        try:
            tf_idf_1 = self.tf_idf_values[document_index][word]
            sort = sorted(self.tf_idf_values[document_index],
                          key=lambda x: (self.tf_idf_values[document_index][x]), reverse=True)
            position = sort.index(word)
            return tuple((tf_idf_1, position))
        except (IndexError, TypeError):
            return ()
        except KeyError:
            return None


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
