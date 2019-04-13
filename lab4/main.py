from lab4.bayes import Bayes


def main():
    bayes = Bayes()
    bayes.load('./cache/bayes.counter.cache.json')
    print('loaded')

    with open('./data/bledy.txt', encoding='UTF-8') as file:
        for i in range(2):
            line = file.readline().rstrip('\n')
            w, c = line.split(';')

            print(w, c)
            best = bayes.get_best_corrections(w)
            print(best)
            # print()
            # print(bayes.p_c(c))


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
    # generate_bayes_cache()
    #
    # d = {}
    # for c in Dictionary().get_words_list():
    #     l = len(c)
    #     if l not in d:
    #         d[l] = []
    #     d[l].append(c)
