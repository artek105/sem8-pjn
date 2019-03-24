from lab1.ngrams import NGrams
from lab2.sjp.dictionary import Dictionary
import matplotlib.pyplot as plt
import json


def main():
    hw4()


def hw4():
    with open('./cache/potop.basics.cache.json') as file:
        data = json.load(file)

        ngrams_2 = NGrams(2)
        ngrams_3 = NGrams(3)
        for word, count in data.items():
            ngrams_2.apply_text(word, count)
            ngrams_3.apply_text(word, count)

        print(ngrams_2.map)
        print(ngrams_3.map)
        pass


def hw3():
    with open('./cache/potop.basics.cache.json') as file:
        data = json.load(file)
        data = sorted(data.items(), key=lambda kv: (kv[1], kv[0]))[::-1]

        length = 0
        hl = 0
        for word, count in data:
            if count == 1:
                hl += 1

            length += count

        half = length / 2
        size = 0
        for word, count in data:
            half -= count
            size += 1

            if half <= 0:
                break

        print('words in text:', len(data))
        print('hapax legomena:', hl)
        print('50% of text consist of:', size, 'words')


def hw2():
    with open('./cache/potop.basics.cache.json') as file:
        data = json.load(file)
        data = sorted(data.items(), key=lambda kv: (kv[1], kv[0]))[::-1]

        n = 50
        y = [y for x, y in data][:n]

        plt.plot(y, 'g')

        # zipf
        k = 25000
        z = [k / x for x in range(1, n)]
        plt.plot(z, 'r', label='zipf')

        # mandelbrot
        P = 37500
        B = 1
        d = .5
        m = [P / ((x + d) ** B) for x in range(1, n)]
        plt.plot(m, 'b', label='mandelbrot')

        plt.legend()
        plt.show()


def create_basics_cache():
    with open('./cache/potop.cache.json', 'r') as file:
        potop = json.load(file)

    basics = {}
    dic = Dictionary()
    for word, count in potop.items():
        basic = dic.get_basic_form(word)

        if basic is None:
            continue

        basics[basic] = (basics[basic] if basic in basics else 0) + count

    with open('./cache/potop.basics.cache.json', 'w') as file:
        json.dump(basics, file)


if __name__ == '__main__':
    main()
