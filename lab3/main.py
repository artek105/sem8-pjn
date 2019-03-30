from lab3.levensthein import Levenshtein
from lab3.LCS import LCS


def main():
    norm = Levenshtein.norm('pióro', 'biurko')
    print(norm)

    norm = LCS.norm('pióro', 'biurko')
    print(norm)


if __name__ == '__main__':
    main()
