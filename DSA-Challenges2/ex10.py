def path_exists(graph, start, target):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node == target:
            return True

        if node not in visited:
            visited.add(node)

            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    stack.append(neighbour)

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(path_exists(graph, "A", "F")) 
print(path_exists(graph, "D", "A"))  