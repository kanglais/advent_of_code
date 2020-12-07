import logging
import collections

logging.basicConfig(level=logging.DEBUG)

def main():
    group_answers = format_input()
    group_totals = sum_of_counts(group_answers)
    logging.info(msg=f'sum of all yes answers is {sum(group_totals)}')

def format_input():
    with open('day6_input.txt', 'r') as f:
        group_answers = f.read().split('\n\n')
    return group_answers

def sum_of_counts(group_answers):
    group_totals = []
    for group in group_answers:
        group = group.split('\n')
        group_yes = 0
        logging.info(msg=f'processing group {group}')
        letters = []
        num_responses = len(group)
        logging.info(msg=f'group size {num_responses}')
        for answer in group:
            answer = answer.strip('\n')
            for x in answer:
                letters.append(x)
        logging.info(msg=f'group yes answers are {letters}')
        counter = collections.Counter(letters)
        logging.info(msg=f'group answers in common are {counter}')
        for item in counter.values():
            if item == num_responses:
                group_yes+=1
        logging.info(msg=f'sum of all yes answers in group is {group_yes}\n')
        group_totals.append(group_yes)
    return group_totals

if __name__ == '__main__':
    main()
