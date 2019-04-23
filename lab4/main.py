from lab4.bayes import Bayes
from threading import Thread
from datetime import datetime


def main():
    bayes = Bayes()
    bayes.load('./cache/bayes.counter.cache.json')
    print('loaded')

    n_threads = 8
    n_res = 10
    results = [0] * n_res

    class CountAccuracyThread(Thread):
        def __init__(self, data, debug=False):
            super().__init__()
            self.data = data
            self.debug = debug

        def run(self):
            for w, c in self.data:
                corrections = bayes.get_best_corrections(w)

                if self.debug:
                    print(w, c, 'corrections:', corrections)

                for i in range(n_res):
                    if i >= len(corrections):
                        break

                    if c == corrections[i]:
                        results[i] += 1
                        break

    with open('./data/bledy.txt', encoding='UTF-8') as file:
        test_data = file.readlines()
        test_data = [line.rstrip('\n').split(';') for line in test_data]

        chunk_size = int(len(test_data) / n_threads) + 1
        chunks = [test_data[i * chunk_size:(i + 1) * chunk_size] for i in range(n_threads)]
        threads = [CountAccuracyThread(chunk, debug=True) for chunk in chunks]

        start = datetime.now()

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = datetime.now()

        print(len(test_data))  # 938
        print(results)  # [438, 73, 28, 23, 14]
        print([r / len(test_data) for r in results])
        print((end - start).total_seconds() / 60, 'min')
        print((end - start).total_seconds() / len(test_data) * n_threads)


def example():
    bayes = Bayes()
    bayes.load('./cache/bayes.counter.cache.json')
    print('loaded')

    w = 'atmoswera'
    c = 'atmosfera'
    print(w, c)
    corrections = bayes.get_best_corrections(w, print_times=True)
    print(corrections)


def generate_bayes_cache():
    bayes = Bayes()
    bayes.apply_file('./data/dramat.txt')
    bayes.apply_file('./data/popul.txt')
    bayes.apply_file('./data/proza.txt')
    bayes.apply_file('./data/publ.txt')
    bayes.apply_file('./data/wp.txt')
    bayes.save('./cache/bayes.counter.cache.json')


if __name__ == '__main__':
    main()
    # example()
    # generate_bayes_cache()
