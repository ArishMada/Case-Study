from graph import map_graph
from collections import deque


def dfs(graph, start, goal):
    OPEN = [(start, [start])]
    visited = []  # already visited nodes
    i = 0

    while OPEN:
        i += 1
        print(f'step ', i)
        for item in OPEN:
            node = item[0]
            print(node, end=',')
        print('\nvisited', visited, '\n')
        node, path = OPEN.pop()  # pop last node and path

        if node == goal:
            return path  # goal found

        visited.append(node)  # Mark node as visited
        # print('visited', visited)

        sorted(graph[node])
        for neighbor in reversed(graph[node]):  # reversed to make sure the smallest one is chosen first
            if neighbor in visited or neighbor in [n for n, _ in OPEN]:
                continue
            else:
                OPEN.append((neighbor, path + [neighbor]))

    return None  # No path found


start_node = 1
goal_node = 20

result_path = dfs(map_graph, start_node, goal_node)

if result_path:
    print("Path from", start_node, "to", goal_node, ":", result_path)
else:
    print("No path found from", start_node, "to", goal_node)