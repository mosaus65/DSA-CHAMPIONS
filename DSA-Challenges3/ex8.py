from collections import deque

def shortest_path(graph, start, target):
    if start == target:
        return [start]

    queue = deque([[start]])

    visited = {start}

    while queue:
        path = queue.popleft()
        current_node = path[-1]


        if current_node == target:
            return path

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)

                queue.append(path + [neighbor])
    return None


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print(shortest_path(graph, "A", "F"))