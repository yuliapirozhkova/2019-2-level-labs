"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    if not isinstance(lines_limit, int) and lines_limit > 0:
        lines_limit = 0
    file = open(path_to_file)
    text_from_file = ''
    if isinstance(lines_limit, int) and lines_limit > 0:
        for a in range(lines_limit):
            text_from_file += file.readline()
    file.close()
    return text_from_file


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    frequencies = {}
    if isinstance(text, str):
        if text.replace(' ', ''):
            text = text.lower()
            text_copy = text
            text = text.replace('\'', '')
            literals = ('\n', '\t', '\a', '\b', '\v', '\r', '\f')
            if text.isspace():
                for i in literals:
                    if i in text:
                        text = text.replace(i, ' ')
            for i in text_copy:
                if not i.isalpha() and i != ' ':
                    text = text.replace(i, ' ')
        text = text.strip()
        words = text.split()
        for i in words:
            frequency = text.count(i)
            frequencies[i] = frequency
    return frequencies


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    frequencies_clean = {}
    if isinstance(frequencies, dict):
        working_stop_words = ()
        if isinstance(stop_words, tuple):
            for el in stop_words:
                if isinstance(el, str) and el not in working_stop_words and el != '':
                    working_stop_words += ((el),)
        for k, v in frequencies.items():
            if isinstance(k, str) and k not in working_stop_words:
                frequencies_clean[k] = v
    return frequencies_clean


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    word_frequency_pare = list(frequencies.items())
    word_frequency_pare.sort(key=lambda n_tuple: n_tuple[1], reverse=True)
    gotten_top_n = ()
    if top_n > len(frequencies):
        top_n = len(frequencies)
    for ind in range(top_n):
        pare = word_frequency_pare[ind]
        gotten_top_n += ((pare[0]),)
    return gotten_top_n


def write_to_file(path_to_file: str, content: tuple):
    file = open(path_to_file, "a")
    if isinstance(content, tuple):
        for word in content:
            file.write(word)
    file.close()


text_1 = """The Zen of Python, by Tim Peters
98
Beautiful is better than ugly.\a
Explicit is better than implicit.
Simple is better than complex.\t
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.*/4
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity. #$
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
top_nn = 4
stop_words_1 = ('tim', 'peters', 'by', 'beautiful', 6, '', 'if')

frequencies = calculate_frequences(text_1)
filter_stop_words(frequencies, stop_words_1)
got_top_n = get_top_n(frequencies, top_nn)
