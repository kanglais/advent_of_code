import logging as log

log.basicConfig(level=log.DEBUG)


def get_jolts(adapters):
    charging_outlet = 0
    one_jolts = 0
    three_jolts = 1

    jolt_path = []

    for i, jolt in enumerate(adapters):
        if jolt <= charging_outlet+3:
            if jolt - charging_outlet == 1:
                one_jolts+=1
            elif jolt - charging_outlet == 3:
                three_jolts+=1
            charging_outlet = jolt
            jolt_path.append(charging_outlet)
    jolt_path.append(charging_outlet + 3)

    log.info(msg=f'jolt diffs are {one_jolts * three_jolts}')

    memo = {0: 1}
    for r in jolt_path:
        memo[r] = memo.get(r - 3, 0) \
                  + memo.get(r - 2, 0) \
                  + memo.get(r - 1, 0)

    return jolt_path

def format_input():
    with open('day10_input.txt', 'r') as file:
        return sorted([int(f.strip('\n')) for f in file.readlines()])

def main():
    adapters = format_input()
    get_jolts(adapters)


if __name__ == '__main__':
    main()
