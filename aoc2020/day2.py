
final_count = 0

with open('day2_input.txt', 'rw') as f:
    for line in f:
        split_line = line.split(':')
        password = split_line[1].strip(' ')
        split_validator = split_line[0].split(' ')
        high_low = split_validator[0].split('-')
        validator = split_validator[1]

        #part1
        # count = 0
        # for letter in password:
        #     if letter == validator:
        #         count+=1
        # if count >= int(high_low[0]) and count <= int(high_low[1]):
        #     final_count+=1

        #part2
        if password[int(high_low[0])-1] == validator and password[int(high_low[1])-1] != validator:
            final_count+=1
        elif password[int(high_low[0])-1] != validator and password[int(high_low[1])-1] == validator:
            final_count+=1

print(final_count)
