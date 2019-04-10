import json


def save_words_num_map(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


def get_words_num_map(filename):
    _map = {}
    with open(filename, encoding='UTF-8') as file:
        for line in file:
            for word in parse_line(line).split():
                if not word:
                    continue
                _map[word] = 1 if word not in _map else (_map[word] + 1)

    return _map


def parse_line(line):
    return ''.join([c for c in line if c.isalpha() or c == ' ' or c == '\''])
