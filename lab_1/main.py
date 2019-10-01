"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
tex1t = ''
te5xt = 6
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
              'it', 'how', 'further', 'was', 'here', 'than', 'from', 'by')


def calculate_frequences(text):

    prohibited_marks = ['.', '-', ':', '\n', '%', "’s", ',', "'", '*', '~', '^', ';', '"', '@', '$', '%', '*', '&', '^',
                        '%', '$']

    if text is None:
        print('none given')
        frequencies = {}
        return frequencies
    else:
        if type(text) is int:
            print('error. string is type int')
            frequencies = {}
            return frequencies
        else:
            if len(text) == 0:
                print('error. empty string')
                frequencies = {}
                return frequencies
            else:
                text_changed = text.lower()
                text_after_split = text_changed.split(' ')
                # print(text_after_split)
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
                # print(result)
                a = result
                for part in a:
                    count = frequencies.get(part, 0)
                    frequencies[part] = count + 1
                frequencies_list = frequencies.keys()
                for parts in frequencies_list:
                    print(parts, frequencies[parts])
                # print(frequencies)
                return frequencies


def filter_stop_words(frequencies, stop_words):
    frequencies_new = frequencies.copy()
    if stop_words is None or frequencies is None:
        print('error!')
        return {}
    for key in list(frequencies_new):
        if str(key).isdigit or key in stop_words:
            frequencies_new.pop(key)
            continue
    # print (frequencies)
    return frequencies_new



#  """
#  Removes all stop words from the given frequencies dictionary
#  """
#  pass

# get_only_words(text)

calculate_frequences(text)
filter_stop_words(frequencies, stop_words)
# prohibited_marks = ['.', '-', ':', '\n', '%', "’s", ',', "'", '*', '~', '^', ';', '"', '@', '$', '%', '*', '&', '^%$']
# frequencies = {}
# text_changed = text.lower()
# text_after_split = text_changed.split(' ')
# print (text_after_split)
# result = []
# for word in text_after_split:
#   if not word.isdigit() and word not in prohibited_marks:
#      clear_word = ''
#     for el in word:
#        if el not in prohibited_marks and not el.isdigit():
#           clear_word += el
#  if clear_word is not '':
#     result.append(clear_word)
# print (result)
# a = result
# for part in a:
#   count = frequencies.get (part,0)
#  frequencies[part] = count + 1
# frequencies_list = frequencies.keys ()
# for parts in frequencies_list:
#    print (parts, frequencies[parts])
# print (frequencies)

# return frequencies

# dictionary_making()


# def dictionary_making ():
# dictionary = {}
# for part in a:
# = dictionary.get (part,0)
# dictionary[part] = count + 1
# dictionary_list = dictionary.keys ()
# for parts in dictionary_list:
# print (parts, dictionary[parts])


# def dictionary (result):
# print (result)


# def resulting (result):
# print (result)
# counter = collections.Counter(result)
# print (counter)
# как разобраться с дефисами, как убрать 's, если запятая поставлена рядом с числом 2011,little

# stop_words = ['the', 'a', 'on', 'in', 'up', 'out', 'as', 'of', 'all' ]

# resulting ()

# def calculate_frequences(text: str) -> dict:
# """
# Calculates number of times each word appears in the text
# """


# def get_top_n(frequencies: dict, top_n: int) -> tuple:
# """
#  Takes first N popular words
# """
# pass
