"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
import re


def calculate_frequences(text) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if not isinstance(text, str):
        dict_1 = {}
    else:
        list_text_all = re.split('[ "#\'!?:;,.\n\-^*~]', text)
        while '' in list_text_all: list_text_all.remove('')
        list_text = [el.lower() for el in list_text_all if el.isalpha()]
        dict_1 = {el: list_text.count(el) for el in list_text}
    return dict_1


def filter_stop_words(dict_2, tpl) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    if isinstance(tpl, tuple) and isinstance(dict_2, dict):
        for k in list(dict_2.keys()):
            if k in tpl or isinstance(k, str) != 1:
                del dict_2[k]
    elif dict_2 is None:
        dict_2 = {}
    return dict_2


def get_top_n(dict_3, top_n) -> tuple:
    """
    Takes first N popular words
    """
    list_dict_3 = []
    if isinstance(top_n, int) and top_n > 0:
        for k in sorted(dict_3, key=dict_3.get, reverse=True):
            if len(list_dict_3) != top_n:
                list_dict_3.append(k)
    return tuple(list_dict_3)








