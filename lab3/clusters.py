class Clusters:
    def __init__(self, norm_func):
        self.clusters = []
        self.item_value_getter = lambda x: x
        self.save_item_value_getter = lambda x: x
        self.boundary_func = lambda i1, i2: .5
        self.norm_func = norm_func

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
