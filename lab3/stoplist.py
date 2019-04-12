from lab2.prepare import get_words_num_map
import re


class StopList:
    static = None
    regexes = {
        r'[^\s]@[^\s]': ' ',
        r'\s[A-Z]\s': ' ',

        # regex to the end of line
        r'\sSA\s.*': '',
        r'\sSP\s.*': '',
        r'\sUL\s.*': '',
        r'\sTEL\s.*': '',
        r'\sRD\s.*': '',
        r'\sSTR\s.*': '',
        r'\sCO\s.*': '',
        r'\sZIP\s.*': '',

        r'\sLLC.*': '',
        r'\sLTD.*': '',
        r'\sFAX.*': '',
        r'\sROAD.*': '',
        r'\sSTREET.*': '',
        r'\sCITY.*': '',
        r'\sDISTRICT.*': '',
        r'\sLIMITED.*': '',

        r'(?<=LOGISTICS).*': ' ',
    }

    @staticmethod
    def apply(line):
        line = StopList.apply_regexes(line)
        line = StopList.apply_static(line)
        return line

    @staticmethod
    def apply_regexes(line):
        for regex, replacement in StopList.regexes.items():
            line = re.sub(regex, replacement, line)

        return line

    @staticmethod
    def apply_static(line):
        words = line.split()
        stoplist = StopList.load_static()
        filtered = ' '.join([word for word in words if word not in stoplist])

        return re.sub(r'\s+', ' ', filtered).strip()

    @staticmethod
    def load_static():
        if StopList.static is not None:
            return StopList.static

        with open('./data/stoplist.txt') as source:
            stoplist = source.readlines()
            stoplist = [item.rstrip('\n') for item in stoplist]
            stoplist = [item for item in stoplist if item]

            StopList.static = stoplist
            return stoplist

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
