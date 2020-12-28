import logging as log
from collections import namedtuple


log.basicConfig(level=log.DEBUG)


def format():
    with open('day11_input.py', 'r') as file:
        return [[x for x in f.strip('\n')] for f in file.readlines()]

# if x or y < 0 or > len then skip it
def get_direction(current_position, seat_row_len, seat_col_len):
    pointer = namedtuple('Pointer', 'x y')

    zero = lambda x: max(x,0)
    roof_row = lambda x: min(x, seat_row_len-1)
    roof_col = lambda x: min(x, seat_col_len-1)

    up = pointer(current_position.x, zero(current_position.y - 1))
    down = pointer(current_position.x, roof_row(current_position.y + 1))
    left = pointer(zero(current_position.x - 1), current_position.y)
    left_up = pointer(left.x, up.y)
    left_down = pointer(left.x, down.y)
    right = pointer(roof_col(current_position.x + 1), current_position.y)
    right_up = pointer(right.x, up.y)
    right_down = pointer(right.x, down.y)

    return [up, down, left, left_up, left_down, right, right_up, right_down]


def check_surrounding_seats(seat_plan, adjacent_seats, current_seat):
    log.info(f'current seat {current_seat}')
    free_seats = 0
    taken_seats = 0

    for direction in set(adjacent_seats):
        if seat_plan[direction.x][direction.y] == 'L' or seat_plan[direction.x][direction.y] == '.':
            free_seats += 1
        if seat_plan[direction.x][direction.y] == '#':
            taken_seats += 1

    if taken_seats >= 4:
        log.info(f'taken seats {taken_seats}')
        return False
    if free_seats == len(set(adjacent_seats)):
        log.info(f'free seats & floor {free_seats}')
        return True

    return False


def sit_down(seat_plan):
    surrounding_seats = namedtuple('Pointer', 'x y')

    for i, row in enumerate(seat_plan):
        for z, seat in enumerate(row):
            if seat_plan[i][z] == 'L':
                current_seat = surrounding_seats(i,z)
                adjacent_seats = get_direction(current_position=current_seat, seat_row_len=len(seat_plan[0]), seat_col_len=len(seat_plan))

                if check_surrounding_seats(seat_plan, adjacent_seats, current_seat):
                    log.info(f'Surrounding seats empty')
                    seat_plan[i][z] = '#'

            elif seat_plan[i][z] == '#':
                current_seat = surrounding_seats(i,z)
                adjacent_seats = get_direction(current_position=current_seat, seat_row_len=len(seat_plan[0]), seat_col_len=len(seat_plan))

                if not check_surrounding_seats(seat_plan, adjacent_seats, current_seat):
                    log.info(f'Surrounding seats full')
                    seat_plan[i][z] = 'L'

    return seat_plan


def count_full_seats(seat_plan):
    count = 0
    for row in seat_plan:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def simulate_seating(seat_plan):
    while True:
        full_seats = count_full_seats(seat_plan)
        updated_seat_plan = sit_down(seat_plan)
        updated_full_seats = count_full_seats(updated_seat_plan)

        if full_seats == updated_full_seats:
            break
        seat_plan = updated_seat_plan

    return full_seats


def main():
    seat_plan = format()
    log.info(f'num of full seats {simulate_seating(seat_plan)}')

if __name__ == '__main__':
    main()
