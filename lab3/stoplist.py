from lab2.prepare import get_words_num_map


class StopList:
    @staticmethod
    def load():
        with open('./data/stoplist.txt') as source:
            stoplist = source.readlines()
            stoplist = [item.rstrip('\n') for item in stoplist]
            return [item for item in stoplist if item]

    @staticmethod
    def automatic(ratio=.2):
        words_map = get_words_num_map('./data/lines.txt')
        data = sorted(words_map.items(), key=lambda kv: (kv[1], kv[0]))[::-1]

        # calculate distinct words count and words count
        length = 0
        hl = 0
        for word, count in data:
            if count == 1:
                hl += 1

            length += count

        # get stoplist words
        half = length * ratio
        stoplist = []
        for word, count in data:
            half -= count
            stoplist.append(word)

            if half <= 0:
                break

        return stoplist
