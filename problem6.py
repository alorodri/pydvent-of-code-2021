import default_test
import my_input

CREATION_DAYS = 7
DAYS_LOOP = 256
buffer = 0

def solution(test):
    fishes = my_input.split_as_type(my_input.get_example(6)[0], ',', int) if test else my_input.split_as_type(my_input.get_input(6)[0], ',', int)
    day_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fish in fishes:
        day_array[fish] += 1

    for day in range(1, DAYS_LOOP + 1):
        buffer = day_array[0]
        for i in range(len(day_array)):
            day_array[i] = day_array[i+1] if i != len(day_array) - 1 else buffer
            if i == len(day_array) - 1:
                day_array[6] += buffer

        print(f"Day {day} completed with {sum(day_array)} fishes")
    return sum(day_array)
    

default_test_passed = default_test.test_default_solution(solution(True), 26984457539)
if default_test_passed:
    print(f"Input result: {solution(False)}")