class Levenshtein:
    @staticmethod
    def norm(word1, word2, strong_comparison=True):
        m = len(word1)
        n = len(word2)

        old_row = [i for i in range(n + 1)]
        new_row = [0] * (n + 1)  # values will be overridden, hence values doesn't meters

        for i1 in range(m):
            ch1 = word1[i1]
            new_row[0] = i1 + 1

            for i2 in range(n):
                ch2 = word2[i2]

                index = i2 + 1
                new_row[index] = min(old_row[index] + 1, new_row[index - 1] + 1)

                if ch1 == ch2:
                    new_row[index] = min(new_row[index], old_row[index - 1])
                elif not strong_comparison and Levenshtein.are_same_weak(ch1, ch2):
                    new_row[index] = min(new_row[index], old_row[index - 1] + .5)
                else:
                    new_row[index] = min(new_row[index], old_row[index - 1] + 1)

            old_row = new_row.copy()

        return new_row[n]

    @staticmethod
    def are_same_weak(c1, c2):
        comparisons = [
            'aą',
            'cć',
            'eę',
            'lł',
            'nń',
            'oóu',
            'sś',
            'zź',
            'rzż',
            'dt',
            'ij',
            'wf'
        ]

        for comp in comparisons:
            if c1 in comp and c2 in comp:
                return True

        return False
