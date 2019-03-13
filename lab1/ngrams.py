class NGrams:
    def __init__(self, n, _map=None):
        self.map = {} if _map is None else _map
        self.n = n

    def fit_by_file(self, filename, encoding=None):
        with open(filename, encoding=encoding, mode='r') as file:
            for line in file:
                self.fit_by_text(line)

    def fit_by_text(self, text):
        for word in self.parse_line(text).split():
            n_grams = self.collect_n_grams(word)
            for n_gram in n_grams:
                count = self.map.get(n_gram)
                new_count = 1 if count is None else (count + 1)
                self.map[n_gram] = new_count

    @staticmethod
    def parse_line(line):
        return ''.join([c for c in line.lower() if c.isalpha() or c == ' ' or c == '\''])

    def collect_n_grams(self, word):
        n_grams = []
        for start in range(len(word) - self.n + 1):
            n_grams.append(word[start:start + self.n])

        return n_grams


def norm(base, n_grams):
    if len(base.map) == 0 or len(n_grams.map) == 0:
        return 1

    _sum = len_base = len_x = 0
    for n_gram, value_base in base.map.items():
        value_x = n_grams.map.get(n_gram)
        value_x = 0 if value_x is None else value_x

        _sum += value_x * value_base
        len_base += value_base ** 2
        len_x += value_x ** 2

    len_base **= .5
    len_x **= .5

    return 1 - _sum / (len_base * len_x)
