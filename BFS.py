from graph import map_graph
from collections import deque


def bfs(graph, start, goal):
    # Keep track of nodes to visit, starting with the start node and its path
    queue = [(start, [start])]
    # Keep track of visited nodes
    visited = []

    i = 0

    # Continue until there are nodes to visit
    while queue:
        i += 1
        print(f'step ', i)
        for item in queue:
            node = item[0]
            print(node, end=',')

        print('\nvisited', visited, '\n')
        # Get the current node and its path from the queue
        node, path = queue.pop(0)

        # If the node has not been visited yet
        if node not in visited:
            # Mark it as visited
            visited.append(node)

            # If this node is the goal, return the path
            print('node:', node)
            if node == goal:
                return path

            # Add adjacent nodes to the queue along with their paths
            for adjacent in graph[node]:
                print('adjacent:', adjacent)
                if adjacent in visited or adjacent in [n for n, _ in queue]:
                    continue
                else:
                    new_path = path + [adjacent]  # Extend the current path
                    queue.append((adjacent, new_path))
                    print('path:', new_path)

    # If goal is not reachable
    return "Goal not reachable"


start_node = 1
goal_node = 20

result_path = bfs(map_graph, start_node, goal_node)

if result_path:
    print("Path from", start_node, "to", goal_node, ":", result_path)
else:
    print("No path found from", start_node, "to", goal_node)