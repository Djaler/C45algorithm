def is_all_equals(items):
    return all(items[0] == item for item in items)


def create_subtable(table, column, variant):
    indices = [index for index, item in enumerate(table[column]) if
               item == variant]
    
    return {
        column: [item for index, item in enumerate(items) if index in indices]
        for column, items in table.items()}


def formalize_rules(list_rules):
    text = []
    for rule in list_rules:
        rule = [part for part in rule.split(',') if part]
        
        text.append('Если {},'.format(rule[0]))
        text.extend(['\t{},'.format(part) for part in rule[1:-1]])
        text.append('То: {}.\n'.format(rule[-1]))
    return '\n'.join(text)


def get_subtables(table, divide_column):
    return [create_subtable(table, divide_column, variant) for variant in
            set(table[divide_column])]
