def get_example(id):
    return get_lines(f"example{id}.txt")

def get_input(id):
    return get_lines(f"input{id}.txt")

def get_lines(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    striped_lines = []
    for line in lines:
        striped_lines.append(line.rstrip())
    return striped_lines

def split_as_type(str, character, type: type):
    values = str.split(character)
    casted_values = []
    for value in values:
        casted_values.append(type(value))
    return casted_values
