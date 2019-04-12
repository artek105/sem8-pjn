class Levenshtein:
    @staticmethod
    def norm(word1, word2):
        old_row = [i for i in range(len(word2) + 1)]
        new_row = [i for i in range(len(word2) + 1)]  # values will be overridden, hence values doesn't meters

        for i1, ch1 in enumerate(word1):
            new_row[0] = i1 + 1

            for i2, ch2 in enumerate(word2):
                index = i2 + 1
                if ch1 == ch2:
                    new_row[index] = min(old_row[index] + 1, old_row[index - 1], new_row[index - 1] + 1)
                else:
                    new_row[index] = min(old_row[index] + 1, old_row[index - 1] + 1, new_row[index - 1] + 1)

            old_row = new_row.copy()

        return new_row[len(word2)]
