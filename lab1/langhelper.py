from ngrams import NGrams
from os.path import exists


languages = [
    'english',
    'finnish',
    'german',
    'italian',
    'polish',
    'spanish',
]

custom_encodings = {
    'italian': 'latin_1',
}


def get_lang_n_grams(lang, n):
    i = 1
    n_grams = NGrams(n)
    while True:
        filename = lang + str(i) + '.txt'
        path = './texts/' + filename
        if not exists(path):
            return n_grams
        n_grams.fit_by_file(path, get_encoding(lang))
        i += 1


def get_encoding(lang):
    return custom_encodings.get(lang)
