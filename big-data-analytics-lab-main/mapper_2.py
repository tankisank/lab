#!/usr/bin/env python

import sys

# Mapper function
def mapper():
    for line in sys.stdin:
        line = line.strip()
        
        # Split the line using any amount of whitespace as a delimiter
        parts = line.split(None, 1)
        
        if len(parts) == 2:
            matrix_id, matrix_data_str = parts
            matrix_id = matrix_id.strip()  # Remove any extra whitespace
            
            # Check if the matrix ID is 'A' or 'B'
            if matrix_id in ('A', 'B'):
                # Convert matrix_data_str to a list by evaluating it
                matrix_data = eval(matrix_data_str)
                
                if matrix_id == 'A':
                    # Iterate over the rows and elements and emit intermediate key-value pairs
                    for i, row in enumerate(matrix_data):
                        for j, value in enumerate(row):
                            # Emit intermediate key-value pairs in the specified format
                            print('{},A,{},{}'.format(i, j, value))
                elif matrix_id == 'B':
                    # Store the vector elements and emit them as key-value pairs
                    for i, value in enumerate(matrix_data):
                        # Emit intermediate key-value pairs in the specified format
                        print('{},B,0,{}'.format(i, value))

if __name__ == "__main__":
    mapper()


