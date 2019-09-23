def calculate_frequences(text: str) -> dict:
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
    if frequencies is None:
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
    if not isinstance(top_n, int):
        return frequencies
    if top_n < 0:
        top_n = 0
    if top_n > len(frequencies):
        top_n = len(frequencies)
    top_words = sorted(frequencies, key=lambda x: int(frequencies[x]), reverse=True)
    best = tuple(top_words[:top_n])
    return best



