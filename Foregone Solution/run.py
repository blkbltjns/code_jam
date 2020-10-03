import sys

def print_output(case_number, delimiter, *args):
    args_joined = delimiter.join([str(a) for a in args])
    print("Case #" + str(case_number) + ": " + args_joined)

number_of_cases = int(sys.stdin.readline())

fours = list([4 * 10**i for i in range(0,10)])

for case_number in range(1, number_of_cases + 1):
    N = int(sys.stdin.readline())
    A = 1
    
    while True:            
        B = N - A
        str_A = str(A)
        str_B = str(B)
        A_four_index = str_A.find('4')
        B_four_index = str_B.find('4')

        if A_four_index == -1 and B_four_index == -1:
            print_output(case_number, ' ', A, B)
            break

        if A_four_index > -1:
            to_add = 10**(len(str_A) - A_four_index - 1)
            to_subtract = A % to_add
            A += (to_add - to_subtract)

        if B_four_index > -1:
            to_add = 10**(len(str_B) - B_four_index - 1)
            to_subtract = A % to_add
            A += (to_add - to_subtract)