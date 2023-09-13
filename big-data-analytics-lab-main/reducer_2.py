#!/usr/bin/env python
import sys

# Initialize variables to store matrix data and the vector
matrix_data = {}
vector = {}

# Reducer function
def reducer():
    for line in sys.stdin:
        line = line.strip()
        parts = line.split(',')
        
        if len(parts) == 4:
            row, matrix_id, col, value = parts
            row, col, value = int(row), int(col), int(value)
            
            if matrix_id == 'A':
                if row not in matrix_data:
                    matrix_data[row] = {}
                matrix_data[row][col] = value
            elif matrix_id == 'B':
                vector[row] = value

    # Perform matrix-vector multiplication and emit the results
    for row, matrix_row in matrix_data.items():
        result = sum(matrix_row[col] * vector[col] for col in matrix_row)
        print('{}\tA,{},{}'.format(row, row, result))

if __name__ == "__main__":
    reducer()

