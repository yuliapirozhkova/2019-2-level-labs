text = """
   Nearly 60 million people live alone in China now. 
   As one of the fastest growing living arrangements in China, representing 14.0% of all Chinese family households in 2011, little is known about who they are, where they are, and what drive this increase.
   We takes a historical look at the temporal and spatial distribution trends of the one-person household based on 1982, 1990 and 2005 individual-level census data. 
   We also conduct multi-level analysis to examine what contextual and individual characteristics contribute to an individual’s propensity to live alone. 
   Results show that economic development and internal migration are crucial factors for the increasing prevalence. There is an increasing spatial heterogeneity in that these households cluster in economically developed areas. 
   Those who live along vary greatly by age, marital status, and socioeconomic status and are motivated by different socioeconomic and cultural factors quite different from the cultural individualism emphasized in the West.
   """
stop_words = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about',
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
              'it', 'how', 'further', 'was', 'here', 'than', 'from', 'by', 'alone')


def calculate_frequences(text):

    prohibited_marks = ['.', '-', ':', '\n', '%', "’s", ',', "'", '*', '~', '^', ';', '"', '@', '$', '%', '*', '&', '^',
                        '%', '$']
    if text is None:
        print('none given')
        frequencies = {}
        return frequencies
    if type(text) is int:
        print('error. string is type int')
        frequencies = {}
        return frequencies
    if len(text) == 0:
        print('error. empty string')
        frequencies = {}
        return frequencies
    text_changed = text.lower()
    text_after_split = text_changed.split(' ')
    result = []
    frequencies = {}
    for word in text_after_split:
        if not word.isdigit() and word not in prohibited_marks:
            clear_word = ''
            for el in word:
                if el not in prohibited_marks and not el.isdigit():
                    clear_word += el
            if clear_word is not '':
                result.append(clear_word)
    for part in result:
        count = frequencies.get(part, 0)
        frequencies[part] = count + 1
    return frequencies


def filter_stop_words(frequencies, stop_words):

    if stop_words is None or frequencies is None or len(frequencies) == 0:
        print('error!')
        return {}
    if type(frequencies) is not dict:
        return {}
    else:
        frequencies_new = frequencies.copy()
        for stop_word in stop_words:
            if isinstance(stop_word, str) and len(stop_word) > 0:
                if frequencies_new.get(stop_word):
                    frequencies_new.pop(stop_word)
        for key in frequencies_new:
            if key in stop_words or isinstance(key, int):
                frequencies_new.pop(key)
                return frequencies_new
    return frequencies_new


def get_top_n(frequencies_new, top_n):

    if frequencies_new == {} or top_n < 0 or top_n == 0:
        return ()
    list_of_top_words = []
    ii = 0
    for n in frequencies_new:
        if ii == top_n:
            break
        list_of_top_words = sorted(frequencies_new, key=lambda n: frequencies_new[n], reverse=True)
        ii += 1
    print(list_of_top_words)
    final_frequencies_tuple = tuple(list_of_top_words[:top_n])
    print(final_frequencies_tuple)
    return final_frequencies_tuple
