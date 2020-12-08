

with open('day1_input.txt', 'rw') as f:
    inputs = [int(i) for i in f]

for input1 in inputs:
    for input2 in inputs:
        for input3 in inputs:
            if input1 + input2 + input3 == 2020:
                print(input1 * input2 * input3)