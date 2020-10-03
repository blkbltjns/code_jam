import sys

def print_output(case_number, delimiter, *args):
    args_joined = delimiter.join([str(a) for a in args])
    print("Case #" + str(case_number) + ": " + args_joined)

def get_first_clauses(patterns):
    first_clauses = []
    for pattern in patterns:
        first_clause = pattern.split('*')[0]
        if (first_clause != ''):
            first_clauses.append(first_clause)
    return first_clauses

def get_last_clauses(patterns):
    last_clauses = []
    for pattern in patterns:
        if ('*' not in pattern):
            continue

        last_clause = pattern.split('*')[-1]
        if (last_clause != ''):
            last_clauses.append(last_clause)
    return last_clauses

def get_collapsed_middle_clauses(patterns):
    collapsed_middle_clauses = []
    for pattern in patterns:
        if (pattern.count('*') < 2):
            continue
        collapsed_middle_clause = ''.join(pattern.split('*')[1 : -1])
        if (collapsed_middle_clause != ''):
            collapsed_middle_clauses.append(collapsed_middle_clause)
    return collapsed_middle_clauses

number_of_cases = int(sys.stdin.readline())

for case_number in range(1, number_of_cases + 1):
    N = int(sys.stdin.readline())
    patterns = []
    first_clauses = []
    for pattern_number in range(0, N):
        pattern = sys.stdin.readline().replace('\n','')
        patterns.append(pattern)
    
    first_clauses = get_first_clauses(patterns)
    collapsed_middle_clauses = get_collapsed_middle_clauses(patterns)
    last_clauses = get_last_clauses(patterns)

    matching_word = ''
    if (len(first_clauses) > 0):
        first_clauses.sort(reverse=True, key=lambda a : len(a))
        longest_first_clause = first_clauses[0]
        if (not all(longest_first_clause.startswith(first_clause) for first_clause in first_clauses)):
            print_output(case_number, '', '*')
            continue

        matching_word += longest_first_clause
    
    for collapsed_middle_clause in collapsed_middle_clauses:
        matching_word += collapsed_middle_clause
    
    if (len(last_clauses) > 0):
        last_clauses.sort(reverse=True, key=lambda a : len(a))
        longest_last_clause = last_clauses[0]
        if (not all(longest_last_clause.endswith(last_clause) for last_clause in last_clauses)):
            print_output(case_number, '', '*')
            continue
        matching_word += longest_last_clause
    
    print_output(case_number, '', matching_word)