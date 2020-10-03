import sys
from array import *

def create_matrix(rows, columns):
    return [[0] * columns for i in range(rows)]

def calculate_trace(a):
    n = len(a)
    trace = 0
    for i in range(0, n):
        trace += a[i][i]
    return trace

def get_num_repeated_rows(a):
    n = len(a)
    num_repeated_rows = 0
    for i in range(0, n):
        s = set()
        
        for j in range(0, n):
            value = a[i][j]
            if (value in s):
                num_repeated_rows += 1
                break
            s.add(value)

    return num_repeated_rows

def get_num_repeated_columns(a):
    n = len(a)
    num_repeated_columns = 0
    for i in range(0, n):
        s = set()
        
        for j in range(0, n):
            value = a[j][i]
            if (value in s):
                num_repeated_columns += 1
                break
            s.add(value)

    return num_repeated_columns

number_of_cases = int(sys.stdin.readline())

for case_number in range(1, number_of_cases + 1):
    n = int(sys.stdin.readline())
    a = create_matrix(n,n)
    for row_index in range(0, n):
        row = sys.stdin.readline()
        columns = row.split()
        for column_index in range(0, n):
            a[row_index][column_index] = int(columns[column_index])

    trace = calculate_trace(a)
    num_repeated_rows = get_num_repeated_rows(a)
    num_repeated_columns = get_num_repeated_columns(a)

    print("Case #" + str(case_number) + ": " + str(trace) + " " + str(num_repeated_rows) + " " + str(num_repeated_columns))  