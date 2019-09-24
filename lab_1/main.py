"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    frequencies = {}
    new_text = ''
    if text is None:
        return frequencies
    if not isinstance(text, str):
        text = str(text)
    for i in text:
        if i.isalpha() or i == ' ':
            new_text += i
    new_text = new_text.lower()
    words = new_text.split()
    for key in words:
        key = key.lower()
        if key in frequencies:
            value = frequencies[key]
            frequencies[key] = value + 1
        else:
            frequencies[key] = 1
    return frequencies


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    if frequencies is None:
        frequencies = {}
        return frequencies
    for i in list(frequencies):
        if not isinstance(i, str):
            del frequencies[i]
    if not isinstance(stop_words, tuple):
        return frequencies
    for i in stop_words:
        if not isinstance(i, str):
            continue
        if frequencies.get(i) is not None:
            del frequencies[i]
    return frequencies


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    :param
    """
    if not isinstance(top_n, int):
        frequencies = ()
        return frequencies
    if top_n < 0:
        top_n = 0
    elif top_n > len(frequencies):
        top_n = len(frequencies)
    top_words = sorted(frequencies, key=lambda x: int(frequencies[x]), reverse=True)
    best = tuple(top_words[:top_n])
    return best


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    """
    Read text from file
    """
    file = open(path_to_file)
    counter = 0
    text = ''
    if file is None:
        return text
    for line in file:
        text += line
        counter += 1
        if counter == lines_limit:
            break
    file.close()
    return text
