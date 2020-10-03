import sys

def print_output(case_number, delimiter, *args):
    args_joined = delimiter.join([str(a) for a in args])
    print("Case #" + str(case_number) + ": " + args_joined)

number_of_cases = int(sys.stdin.readline())

for case_number in range(1, number_of_cases + 1):
    parameters = list([int(x) for x in sys.stdin.readline().split()])
    N = int(sys.stdin.readline().split()[0])
    
    primes = set()
    numbers = list([int(x) for x in sys.stdin.readline().split()])

    for i in range(0, len(numbers) - 1):
        first = numbers[i]
        for j in range(i + 1, len(numbers)):
            second = numbers[j]

        

    print_output(case_number, '', [])