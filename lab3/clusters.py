from lab1.main import print_stats


class Clusters:
    def __init__(self):
        self.clusters = []
        self.item_value_getter = lambda x: x
        self.save_item_value_getter = lambda x: x
        self.boundary_func = lambda i1, i2: .5
        self.norm_func = lambda i1, i2: 1

    def add_items(self, items):
        i = 0
        for item in items:
            i += 1

            self.add_item(item)

            if i % 50 == 0:
                print(i)

        return self

    def set_boundary_func(self, boundary_func):
        self.boundary_func = boundary_func

        return self

    def set_item_value_getter(self, item_value_getter):
        self.item_value_getter = item_value_getter

        return self

    def set_save_item_value_getter(self, save_item_value_getter):
        self.save_item_value_getter = save_item_value_getter

        return self

    def set_norm_func(self, norm_func):
        self.norm_func = norm_func

        return self

    def add_item(self, new_item):
        best_chance = None  # (norm, cluster)
        i = 0
        for cluster in self.clusters[::-1]:
            for item in cluster[::-1]:
                i += 1
                if i > 20:
                    break

                item_value_1 = self.item_value_getter(item)
                item_value_2 = self.item_value_getter(new_item)
                norm = self.norm_func(item_value_1, item_value_2)
                boundary = self.boundary_func(item_value_1, item_value_2)

                # if norm is so close, add item to cluster without chances
                if norm <= boundary / 2:
                    cluster.append(new_item)
                    return

                # look for the best chance
                if norm <= boundary and (best_chance is None or norm < best_chance[0]):
                    best_chance = (norm, cluster)

            if i > 2000:
                break

        if best_chance is not None:
            best_chance[1].append(new_item)
        else:
            self.clusters.append([new_item])

    def count_clusters(self):
        return len(self.clusters)

    def count_items(self):
        return sum([len(cluster) for cluster in self.clusters])

    def save(self, filename):
        with open(filename, mode='w') as file:
            file.write(str(self.count_clusters()) + '\n' * 2)

            for cluster in self.clusters:
                file.write('#' * 20 + '\n')
                for item in cluster:
                    value = self.save_item_value_getter(item)
                    file.write(value + '\n')
                file.write('\n')

    @staticmethod
    def load(filename):
        instance = Clusters()
        with open(filename) as file:
            cluster = None
            for line in file:
                line = line.rstrip('\n')

                if line == '####################':
                    if cluster is not None:
                        instance.clusters.append(cluster)
                    cluster = []
                    continue

                if cluster is None or not line:
                    continue

                cluster.append(line)

            if cluster is not None:
                instance.clusters.append(cluster)

            return instance

    # returns cluster and item indexes
    def get_cluster_index_by_item(self, search):
        for index, cluster in enumerate(self.clusters):
            if search in cluster:
                return index
        return None

    def print_stats(self, other):
        true_positive = true_negative = false_positive = false_negative = 0

        clusters_mapping = self.get_clusters_mapping(other)
        for cm, cluster in zip(clusters_mapping, self.clusters):
            indexes = [other.get_cluster_index_by_item(item) for item in cluster]
            true_positive += indexes.count(cm)
            false_negative += len(indexes) - indexes.count(cm)

        print_stats(true_positive, false_positive, false_negative, true_negative)

    # map self.clusters to other.clusters index
    def get_clusters_mapping(self, other):
        mapped_to_indexes = [[other.get_cluster_index_by_item(item) for item in cluster] for cluster in self.clusters]
        filtered = [[j for j in i if j is not None] for i in mapped_to_indexes]
        return [max(indexes, key=indexes.count) if len(indexes) else None for indexes in filtered]
