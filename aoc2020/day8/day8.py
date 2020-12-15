import logging as log

log.basicConfig(level=log.DEBUG)


def run_through_rules(rules):
    accumulator = 0
    rule_index = 0
    seen = set()

    while True:
        rule = rules[rule_index]

        if rule_index in seen:
            return 1, accumulator
        elif rule_index == len(rules):
            return 0, accumulator

        seen.add(rule_index)
        log.info(msg=f'rule index: {rule_index}')
        log.info(msg=f'rule: {rule}')
        log.info(msg=f'accumulator: {accumulator}')

        if rule[0] == 'nop':
            rule_index += 1
        elif rule[0] == 'acc':
            rule_index += 1
            accumulator += int(rule[1])
        elif rule[0] == 'jmp':
            rule_index += int(rule[1])


def format():
    with open('day8_input.txt', 'r') as f:
        rules = [[x.strip('\n').strip() for x in line.split(' ')] for line in f.readlines()]
    return rules

def main():
    rules = format()

    for index, (rule, arg) in enumerate(rules):
        if rule in {'jmp', 'nop'}:
            if rule == 'jmp':
                rules[index] = 'nop', arg
            elif rule == 'nop':
                rules[index] = 'jmp', arg
        retcode, accumulator = run_through_rules(rules)
        if retcode == 0:
            return accumulator
        else:
            rules[index] = rule, arg

if __name__ == '__main__':
    main()
