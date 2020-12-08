import logging

logging.basicConfig(level=logging.DEBUG)


def bags_contain_bag(all_the_rules, bag_color, new_bag_colors):
    color_list = []
    logging.info(msg=f'bag color is {bag_color}')
    for rule in all_the_rules:
        for bag in rule[1]:
            if bag_color in bag:
                logging.info(msg=f'bag color {bag_color} is in {bag}')
                color_list.append(rule[0])
    new_bag_colors.extend(color_list)
    while len(color_list) != 0:
        for bag in new_bag_colors:
            bags_contain_bag(all_the_rules, bag, new_bag_colors)
    return new_bag_colors


def format_input():
    all_the_rules = []
    with open('day7_input.txt', 'r') as file:
        for f in file.readlines():
            rule = f.split('contain')
            rule[1] = rule[1].split(',')

            all_the_rules.append(rule)
    for rule in all_the_rules:
        rule[0] = rule[0].strip(' ')

    return all_the_rules


def main(bag_color):
    all_the_rules = format_input()
    new_bag_colors = []
    bags_contain_bag(all_the_rules, bag_color, new_bag_colors)
    return len(new_bag_colors)


if __name__ == '__main__':
    bag_color = 'shiny gold'
    logging.info(f'total bags is {main(bag_color)}')
