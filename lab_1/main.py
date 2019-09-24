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


def write_to_file(path_to_file: str, content: tuple):
    """
    Creates new file
    """
    file = open(path_to_file, 'w')
    for i in content:
        file.write(i)
        file.write('\n')
    file.close()


stop = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about',
        'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be',
        'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself',
        'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
        'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
        'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should',
        'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',
        'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in',
        'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
        'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has',
        'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
        'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing',
        'it', 'how', 'further', 'was', 'here', 'than')

data = read_from_file('Data.txt', 6)
dictionary = calculate_frequences(data)
dictionary = filter_stop_words(dictionary, stop)
rating = get_top_n(dictionary, 10)
write_to_file('report.txt', rating)
