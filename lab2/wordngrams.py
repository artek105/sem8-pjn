from lab1.ngrams import NGrams


class WordNGrams(NGrams):
    def apply_text(self, text, count=1):
        words = self.parse_line(text).split()
        n_grams = self.collect_n_grams(words)
        for n_gram in n_grams:
            self.map[n_gram] = count if n_gram not in self.map else (self.map[n_gram] + count)

    def collect_n_grams(self, words):
        n_grams = []
        for start in range(len(words) - self.n + 1):
            n_grams.append(" ".join(words[start:start + self.n]))

        return n_grams
