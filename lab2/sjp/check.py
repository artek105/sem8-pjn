from lab2.sjp.dictionary import Dictionary


def main():
    max_sub = 20
    with open(Dictionary.varieties_filename, encoding='UTF-8') as file:
        for line in file:
            words = line.split(', ')
            basic = words[0]

            if len(words) < 2 or basic == '?':
                continue

            while True:
                sub = basic[:max_sub]
                if all_starts_with(words, sub):
                    break
                if max_sub < 2:
                    print(words)
                max_sub -= 1

    print(max_sub)


def all_starts_with(_list, _sub):
    for item in _list:
        if not item.startswith(_sub):
            return False
    return True


if __name__ == '__main__':
    main()
