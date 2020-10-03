import sys

def print_output(case_number, delimiter, *args):
    args_joined = delimiter.join([str(a) for a in args])
    print("Case #" + str(case_number) + ": " + args_joined)

number_of_cases = int(sys.stdin.readline())

for case_number in range(1, number_of_cases + 1):
    print_output(case_number, '', [])