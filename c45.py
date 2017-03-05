import math

import utils


def info(table, res_col):
    freqs = []
    for variant in set(table[res_col]):
        freqs.append(table[res_col].count(variant) / len(table[res_col]))
    return -sum(freq * math.log(freq, 2) for freq in freqs)


def info_x(table, col, res_col):
    return sum(len(subtable[col]) / len(table[col]) * info(subtable, res_col)
               for subtable in utils.get_subtables(table, col))


def gain(table, col, res_col):
    return info(table, res_col) - info_x(table, col, res_col)
