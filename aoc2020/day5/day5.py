import math
import logging

logging.basicConfig(level=logging.DEBUG)

with open('day5_input.txt', 'r') as f:
    taken_seats = list(f.readlines())

def get_place(placement, zone):
    halfway = (zone[0] + zone[1]) / 2

    if placement == 'F' or placement == 'L':
        new_zone = [zone[0], math.floor(halfway)]
    elif placement == 'B' or placement == 'R':
        new_zone = [round(halfway), zone[1]]
    return new_zone

def get_final(placement, zone):
    if placement in ['B', 'R']:
        return zone[1]
    else:
        return zone[0]

def get_seat_id(final_row, final_seat):
    return (final_row * 8) + final_seat

def main():
    seats = []
    for seat in taken_seats:
        logging.info(msg=f'processing {seat}')
        zone = [0,127]
        column = [0, 7]
        for place in seat:
            if place in ['F', 'B']:
                zone = get_place(place, zone)
            if place in ['L', 'R']:
                column = get_place(place, column)
            final_row = get_final(seat[6], zone)
            final_seat = get_final(seat[9], column)
        seat_id = get_seat_id(final_row, final_seat)
        seats.append(seat_id)
        logging.info(msg=f'final row is {final_row}')
        logging.info(msg=f'final seat is {final_seat}')
        logging.info(msg=f'seat id is {seat_id}\n')

    logging.info(msg=f'highest seat id is {max(seats)}\n')

    missing_seat = [x for x in range(seats[0], seats[-1]+1) if x not in seats]
    logging.info(msg=f'your seat id is {missing_seat[0]}')

if __name__ == "__main__":
    main()