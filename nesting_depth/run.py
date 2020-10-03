import sys

class Group:
    def __init__(self, number):
        self.number = number
        self.count = 0
        self.left_parens = 0
        self.right_parens = 0

def split(word): 
    return [char for char in word]

def create_groups_text(groups):
    buffer = ''
    for group in groups:
        for i in range(0, group.left_parens):
            buffer += '('
        for i in range(0, group.count):
            buffer += str(group.number)
        for i in range(0, group.right_parens):
            buffer += ')'
    return buffer

def create_groups(numbers):
    groups = []
    previous_number = None

    for number in numbers:
        if number != previous_number:
            current_group = Group(int(number))
            groups.append(current_group)
            current_group.count += 1
        else:
            current_group.count += 1
        previous_number = number

    return groups

def add_initial_parens(groups):
    for group in groups:
        group.left_parens = group.number
        group.right_parens = group.number

def remove_redundant_parens(groups):
    for i in range(0, len(groups) - 1):        
        group = groups[i]
        right_group = groups[i+1]

        num_parens_overlapping = min(group.right_parens, right_group.left_parens)
        group.right_parens = group.right_parens - num_parens_overlapping
        right_group.left_parens = right_group.left_parens - num_parens_overlapping

number_of_cases = int(sys.stdin.readline())
for case_number in range(1, number_of_cases + 1):
    line = sys.stdin.readline()
    numbers = split(line[0:len(line)-1])
    groups = create_groups(numbers)
    add_initial_parens(groups)
    remove_redundant_parens(groups)
    print("Case #" + str(case_number) + ": " + create_groups_text(groups))