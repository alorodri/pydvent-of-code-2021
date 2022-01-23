from nntplib import decode_header
import default_test
import my_input

mean = 0
most_rep = 0

def most_frequent(List):
	return max(set(List), key = List.count)

def calc_fuel(data, i):
    fuel_cost = 0
    for crab in data:
        fuel_cost += abs(crab - i)
    
    return fuel_cost

def calc_fuel_2nd_part(data, i):
    fuel_cost = 0
    for crab in data:
        total_fuel_cost = sum(range(1, abs(crab - i) + 1))
        fuel_cost += abs(total_fuel_cost)

    print(f"Total fuel cost was {fuel_cost} for {i}")
    return fuel_cost

def solution(test):
    fuel_cost_result = 0
    data = my_input.split_as_type(my_input.get_example(7)[0], ',', int) if test else my_input.split_as_type(my_input.get_input(7)[0], ',', int)
    mean = round(sum(data) / len(data))
    most_rep = most_frequent(data)
    diff = abs(mean - most_rep)
    for i in range(mean - diff, mean + diff + 1):
        fuel_cost = calc_fuel_2nd_part(data, i)

        if fuel_cost_result == 0 or fuel_cost < fuel_cost_result:
            fuel_cost_result = fuel_cost

    return fuel_cost_result

default_test_passed = default_test.test_default_solution(solution(True), 168)
if default_test_passed:
    print(f"Input result: {solution(False)}")