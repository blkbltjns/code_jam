import sys
import pdb

def print_output(case_number, delimiter, *args):
    args_joined = delimiter.join([str(a) for a in args])
    print("Case #" + str(case_number) + ": " + args_joined)

number_of_cases = int(sys.stdin.readline())

for case_number in range(1, number_of_cases + 1):
    N = int(sys.stdin.readline())

    lydia_moves = list(sys.stdin.readline().replace('\n', ''))
    me_moves = []
    for lydia_move in lydia_moves:
        if lydia_move == 'E':
            me_moves.append('S')
        else:
            me_moves.append('E')
    print_output(case_number, '', ''.join(me_moves))