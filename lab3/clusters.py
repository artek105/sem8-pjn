import os
import json


class Clusters:
    norm_func = None
    boundary = None
    item_parser = None

    def __init__(self):
        self.clusters = []
        self.items = []  # (item, parsed item)
        self.norms = []

    def set_norm_func(self, norm_func):
        self.norm_func = norm_func

        return self

    def set_boundary(self, boundary):
        self.boundary = boundary

        return self

    def set_item_parser(self, item_parser):
        self.item_parser = item_parser

        return self

    def apply_item(self, item):
        self.items.append(item)

        return self

    def set_items(self, items):
        self.items = items

        return self

    def calculate(self, norms_cache_filename=None):
        assert self.norm_func is not None
        assert self.boundary is not None
        assert self.item_parser is not None

        norms_map = self.calculate_norms_map(norms_cache_filename)

        # parsed = self.item_parser(item)
        #
        # min_norm = self.boundary * 10
        # min_norm_cluster = None
        #
        # for cluster in self.clusters:
        #     avg_norm = 0
        #     for c_parsed in cluster[1]:
        #         avg_norm += self.norm_func(parsed, c_parsed)
        #     avg_norm /= len(cluster)
        #
        #     if avg_norm < min_norm:
        #         min_norm = avg_norm
        #         min_norm_cluster = cluster
        #
        #     if avg_norm < self.boundary / 2:
        #         break
        #
        # if min_norm < self.boundary:
        #     min_norm_cluster[0].append(item)
        #     min_norm_cluster[1].append(parsed)
        # else:
        #     cluster = ([item], [parsed])
        #     self.clusters.append(cluster)

        return norms_map

    def calculate_norms_map(self, cache_filename=None):
        if os.path.exists(cache_filename) and os.path.isfile(cache_filename):
            norms_map = json.load(open(cache_filename))

            return norms_map

        prepared = self.prepare_items()

        size = len(self.items)
        norms_map = {}
        for i1 in range(size):
            print(i1)
            for i2 in range(i1 + 1, size):
                norm = self.norm_func(prepared[i1][1], prepared[i2][1])
                norms_map[(i1, i2)] = norm

        with open(cache_filename, 'w') as file:
            json.dump(norms_map, file)

        return norms_map

    def prepare_items(self):
        return [(item, self.item_parser(item)) for item in self.items]

    def size(self):
        return len(self.clusters)

    # refactor it
    def save(self, filename):
        with open(filename, mode='w') as file:
            file.write(str(self.size()) + '\n' * 2)

            for cluster in self.clusters:
                file.write('#' * 20 + '\n')
                for item in cluster[0]:
                    file.write(item + '\n')
                file.write('\n')
