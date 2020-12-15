import logging as log

log.basicConfig(level=log.DEBUG)

# def add_numbers(numbers, index):
#     sub_list = numbers[:index]
#     count = 0
#
#     while True:
#         log.info(msg=f'checking segment {sub_list}')
#
#         target = numbers[index]
#         valid_list = []
#         log.info(msg=f'target number is {target}')
#
#         for i in sub_list:
#             for z in sub_list:
#                 if i + z == target and i != z:
#                     log.info(msg=f'adding {i} + {z} for {i + z}\n')
#                     valid_list.append(target)
#
#         if target not in valid_list:
#             return target
#         else:
#             index += 1
#             count += 1
#             sub_list = numbers[count:index]


def add_numbers(numbers):
    target = 1398413738

    for i, num1 in enumerate(numbers):
        for z, num2 in enumerate(numbers):
            sub_list = numbers[i:z]
            if sum(sub_list) == target:
                return_list = sorted(sub_list)
                return return_list[0] + return_list[-1]
            elif sum(sub_list) > target:
                sub_list.pop(0)


def format_input():
    with open('day9_input.txt', 'r') as file:
        return [int(f.strip('\n')) for f in file.readlines()]

def main():
    numbers = format_input()

    log.info(msg=f'something happened {add_numbers(numbers)}')


if __name__ == '__main__':
    main()
