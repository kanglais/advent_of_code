import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    group_answers = format_input()
    group_totals = sum_of_counts(group_answers)
    print(group_totals)
    print(len(group_totals))
    logging.info(msg=f'sum of all yes answers is {sum(group_totals)}')

def format_input():
    group_answers = []
    with open('day6_input.txt', 'r') as f:
        group = []
        for line in f.readlines():
            if line == '\n':
                group_answers.append(group)
                group = []
            else:
                group.append(line.strip('\n'))
    return group_answers

def sum_of_counts(group_answers):
    group_totals = []
    for group in group_answers:
        logging.info(msg=f'processing group {group}')
        letters = []
        for answer in group:
            for x in answer:
                if x not in letters:
                    letters.append(x)
        logging.info(msg=f'group yes answers are {letters}\n')
        logging.info(msg=f'sum of all yes answers in group is {len(letters)}\n')
        group_totals.append(len(letters))
    return group_totals

if __name__ == '__main__':
    main()