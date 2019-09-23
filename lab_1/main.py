"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
import re

def calculate_frequences(text):
    if not isinstance(text, str):
        dictionary = {}
    else:
        list_text_all = re.split('[ "#\'\[\]!?:;,.\n\-^*+~]', text)
        while '' in list_text_all: list_text_all.remove('')
        # print(list_text_all)
        list_text = []
        for i in range(len(list_text_all)):
            if list_text_all[i].isalpha():
                list_text.append(list_text_all[i].lower())
        # print(list_text)
        list_freq = []
        for i in range(len(list_text)):
            list_freq.append(list_text.count(list_text[i]))
        # print(list_freq)
        dictionary = {list_text[i]: list_freq[i] for i in range(len(list_text))}
    return dictionary

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    pass


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    pass
