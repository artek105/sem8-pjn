class LCS:  # longest common substring
    def __init__(self, word1, word2):
        self.w1 = word1
        self.w2 = word2

    def calc_recursive(self, i, j, count):
        if i == 0 or j == 0:
            return count

        if self.w1[i - 1] == self.w2[j - 1]:
            count = self.calc_recursive(i - 1, j - 1, count + 1)

        return max(count, max(self.calc_recursive(i, j - 1, 0), self.calc_recursive(i - 1, j, 0)))

    def calc_len(self):
        return self.calc_recursive(len(self.w1), len(self.w2), 0)

    @staticmethod
    def norm(word1, word2):
        instance = LCS(word1, word2)
        return 1 - instance.calc_len() / max(len(word1), len(word2))
