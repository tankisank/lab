import sys

def main():
    current_edge = None
    current_sum = 0

    for line in sys.stdin:
        line = line.strip()
        edge, val = line.split('\t', 2)
        edge = (edge[1:-1]).split(', ')
        val = int(val)

        if current_edge == edge:
            current_sum += val
        else:
            if current_edge:
                print(f"{current_edge}\t{current_sum}")
            current_edge = edge
            current_sum = val

    if current_edge:
        print(f"{current_edge}\t{current_sum}")

if __name__ == '__main__':
    main()
