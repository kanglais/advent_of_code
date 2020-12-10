import logging
import re

logging.basicConfig(level=logging.DEBUG)

# def bags_contain_bag(all_the_rules, bag_color, new_bag_colors):
#     parent_list = get_parent_bags(all_the_rules, bag_color)
#     if len(parent_list) == 0:
#         return new_bag_colors
#     logging.info(msg=f'new bag colors {new_bag_colors}')
#
#     for bag in parent_list:
#         new_bag_colors.add(bag)
#         bags_contain_bag(all_the_rules, bag, new_bag_colors)
#     return new_bag_colors

def get_child_bags(all_the_rules, bag_color):
    logging.info(msg=f'\nbag color is {bag_color}')
    child_nodes = {}

    if all_the_rules[bag_color]:
        for child in all_the_rules[bag_color]:
            child_nodes.update({child: all_the_rules[bag_color][child]})

    logging.info(msg=f'childs {child_nodes}')
    return child_nodes


def count_internal_bags(all_the_rules, bag_color, total_inner_bags=1):
    child_tuple = get_child_bags(all_the_rules, bag_color)

    if child_tuple == {}:
        logging.info("No children returning total inner bags {}".format(total_inner_bags))
        return total_inner_bags

    current_count = 0

    for bag in child_tuple:
        inner_bags = count_internal_bags(all_the_rules, bag, total_inner_bags)
        logging.info(f"Adding {bag} by that bag number {child_tuple[bag]} * inner bags {inner_bags}")
        current_count += (child_tuple[bag] * inner_bags)
        logging.info(msg=f'added {child_tuple[bag] * inner_bags} to total {total_inner_bags}\n')

    logging.info(f"Adding running total {current_count} to {total_inner_bags} for {total_inner_bags + current_count}")
    total_inner_bags += current_count

    logging.info(msg=f'total inner bags {total_inner_bags}\n')
    return total_inner_bags

def format_input():
    all_the_rules = {}
    with open('day7_input.txt', 'r') as file:
        for f in file.readlines():
            rule = f.split('contain')
            rule[1] = rule[1].split(',')

            clean_parent = re.search('(.* .* )(bag|bags)', rule[0]).groups()[0].strip()

            child_list = list(map(lambda bag: re.search('(.* .* .*)(bag|bags)', bag).groups()[0].strip(), rule[1]))
            all_the_rules[clean_parent] = {}
            for i in child_list:
                child = i.split(' ')
                if child[0] == 'no':
                    pass
                else:
                    all_the_rules[clean_parent].update({i[1:].strip(' '): int(child[0])})
    return all_the_rules

def main(bag_color):
    all_the_rules = format_input()
    total_inner_bags = count_internal_bags(all_the_rules, bag_color)
    return total_inner_bags - 1


if __name__ == '__main__':
    bag_color = 'shiny gold'
    logging.info(f'total bags is {main(bag_color)}')
