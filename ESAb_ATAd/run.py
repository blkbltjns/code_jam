import sys
import pdb

def query_position(position):
    print(position, flush=True)
    response = int(sys.stdin.readline())
    return response

def query_positions(position_a, position_b):
    return query_position(position_a), query_position(position_b)

#pdb.set_trace()
log = open("log.txt", "w", buffering=1)

log.write('reading number of test cases and bits\n')
number_of_test_cases, number_of_bits = map(int,sys.stdin.readline().split())
log.write(f'Read {number_of_test_cases} {number_of_bits}\n')

for case_number in range(1, number_of_test_cases + 1):
    same_value_positions = None
    different_value_positions = None
    outside_in_positions = [1, number_of_bits]

    for round_number in range(1, 15):                
        for query_number_in_round in range(1, 10):
            if same_value_positions == None or different_value_positions == None:
                left_value, right_value = query_positions(outside_in_positions(0), outside_in_positions(1))
                if left_value == right_value and same_value_positions == None:
                    same_value_positions = outside_in_positions.copy()
                elif left_value != right_value and different_value_positions == None:
                    different_value_positions = outside_in_positions.copy()

                            

        outside_in_positions[0] += 1
        outside_in_positions[1] -= 1


        # log.write('writing 1\n')
        # print(1, flush=True)
        # log.write('reading response\n')
        # response = int(sys.stdin.readline())
        # log.write(f'read {response}\n')

    log.write(f'writing {number_of_bits * "0"}\n')
    print( number_of_bits * '0' , flush=True)

    log.write(f'reading is_correct_answer\n')
    is_correct_answer = sys.stdin.readline().rstrip('\n')
    log.write(f'read {is_correct_answer}\n')
    if is_correct_answer == 'N':
        log.write(f'exiting\n')
        exit()