class LCS:  # longest common substring
    @staticmethod
    def calc_len(x, y):
        m = len(x)
        n = len(y)

        old_row = [0] * (n + 1)
        new_row = [0] * (n + 1)

        result = 0
        for i in range(m + 1):
            for j in range(1, n + 1):
                if j != 0 and x[i - 1] == y[j - 1]:
                    new_row[j] = old_row[j - 1] + 1
                    result = max(result, new_row[j])

            old_row = new_row
            new_row = [0] * (n + 1)

        return result

    @staticmethod
    def norm(x, y):
        return 1 - LCS.calc_len(x, y) / max(len(x), len(y))

