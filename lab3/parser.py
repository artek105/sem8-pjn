from lab3.stoplist import StopList


class Parser:
    @staticmethod
    def parse(line):
        parsed = Parser.parse_line(line)
        filtered = Parser.apply_stoplist(parsed)

        return filtered.strip()

    @staticmethod
    def apply_stoplist(line):
        words = line.split(' ')
        return ' '.join([word for word in words if word not in StopList.load()])

    @staticmethod
    def parse_line(line):
        return ''.join([c if Parser.is_valid_char(c) else ' ' for c in line.upper()]).strip()

    @staticmethod
    def is_valid_char(c):
        return c.isalpha() or c == ' ' or c == '\''
