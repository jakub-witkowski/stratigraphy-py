class Tiepoint:
    def __init__(self, id, type, label, min_depth, max_depth, age):
        self.id = id
        self.type = type
        self.label = label
        self.min_depth = min_depth
        self.max_depth = max_depth
        self.age = age


class Site:
    def __init__(self, site_number, hole):
        self.site_number = site_number
        self.hole = hole


def average_depth(min_depth, max_depth):
    return (min_depth + max_depth) / 2
