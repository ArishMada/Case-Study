from graph import map_graph


def dfs(graph, current_node, goal, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []

    visited.append(current_node)
    path = path + [current_node]
    print(visited)

    if current_node == goal:
        return path

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path)
            if new_path:
                return new_path

    return None


start_node = 1
goal_node = 20

result_path = dfs(map_graph, start_node, goal_node)

if result_path:
    print("Path from", start_node, "to", goal_node, ":", result_path)
else:
    print("No path found from", start_node, "to", goal_node)
