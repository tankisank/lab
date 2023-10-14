import itertools

def calculate_betweenness(person):
    visited = set()
    queue = [(person, 0)]
    parents = {}
    centrality = {person: 0}

    while queue:
        current, depth = queue.pop(0)
        visited.add(current)

        for neighbor in adjacency_list[current]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
                parents[neighbor] = parents.get(neighbor, []) + [current]

        if depth > 0:
            for child, _ in queue:
                centrality[child] = centrality.get(child, 0) + 1

    return [(edge, 1) for child in centrality for edge in itertools.combinations(parents[child], 2)]

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

    adjacency_list = {}
    for line in lines:
        person1, person2 = line.split()
        adjacency_list.setdefault(person1, []).append(person2)
        adjacency_list.setdefault(person2, []).append(person1)

    input_data = list(adjacency_list.keys())

    for person in input_data:
        results = calculate_betweenness(person)
        for edge, val in results:
            print(f"{edge[0]}\t{edge[1]}\t{val}")

if __name__ == '__main__':
    main()
