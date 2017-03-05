from c45 import gain
from utils import formalize_rules, get_subtables, is_all_equals


def mine_c45(table, result):
    column = max([(column, gain(table, column, result)) for column in table if
                  column != result], key=lambda x: x[1])[0]
    
    tree = []
    for subtable in get_subtables(table, column):
        variant = subtable[column][0]
        if is_all_equals(subtable[result]):
            tree.append(['{} = {}'.format(column, variant),
                         '{} = {}'.format(result, subtable[result][0])])
        else:
            del subtable[column]
            tree.append(
                ['{} = {}'.format(column, variant)] + mine_c45(subtable,
                                                               result))
    return tree


def tree_to_rules(tree):
    return formalize_rules(_tree_to_rules(tree))


def _tree_to_rules(tree, rule=''):
    rules = []
    for node in tree:
        if isinstance(node, str):
            rule += node + ','
        else:
            rules.extend(_tree_to_rules(node, rule))
    
    return rules if rules else [rule]
