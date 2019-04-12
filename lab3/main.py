from lab3.parser import Parser
from lab3.clusters import Clusters
from lab3.levensthein import Levenshtein
from lab3.LCS import LCS


def main():
    with open('./data/lines.txt') as file:
        lines = file.readlines()
        parsed = [(line.rstrip('\n'), Parser.parse(line)) for line in lines]
        filtered = [item for item in parsed if item[1]]
        filtered.sort(key=lambda x: x[1])

        print('items prepared')

        clusters = Clusters(LCS.norm)\
            .set_item_value_getter(lambda t: t[1])\
            .set_save_item_value_getter(lambda i: i[0])\
            .set_boundary_func(get_boundary)\
            .add_items(filtered)

        print(clusters.count_clusters())  # 3356
        clusters.save('./output/clusters.lcs.4.txt')


def get_boundary(item1, item2):
    return .4


def test_norm():
    a = 'ACTONA COMPANY A/S SMEDEGARDSVEJ 6A, TVIS DK-7500 HOLSTEBRO, DENMARK'
    b = 'ACTONA COMPANY A/S SMEDEGAARDVEJ 6A,TVIS 7500, HOLSTEBRO,DENMARK'

    print(a)
    print(b)

    a = Parser.parse(a)
    b = Parser.parse(b)

    print(a)
    print(b)

    print(Levenshtein.norm(a, b))


if __name__ == '__main__':
    main()
    # test_norm()
