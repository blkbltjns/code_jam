from math import inf

graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
h = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

def djikstras(graph, start, finish):
    visited = set()
    shortest_path = []

    not_visited = set((k for k in graph))
    shortest_distance = {}
    for node in not_visited:
        shortest_distance[node] = inf
    shortest_distance[start] = 0
    predecessor_node = {}

    while not_visited:

        # Use a priority queue
        min_node = None
        for node in not_visited:
            if min_node == None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for next_node, weight in graph[min_node].items():
            potential_next_node_cost = shortest_distance[min_node] + weight
            if potential_next_node_cost < shortest_distance[next_node]:
                shortest_distance[next_node] = potential_next_node_cost
                predecessor_node[next_node] = min_node

        not_visited.remove(min_node)

    current_node = finish
    shortest_path.append(current_node)
    while current_node != start:
        previous = predecessor_node[current_node]
        shortest_path.append(previous)
        current_node = previous

    shortest_path.reverse()
    return shortest_path

def a_star(graph, h, start, finish):
    unvisited_nodes = set((x for x, y in graph.items()))
    shortest_distance = {}
    previous_node_in_path = {}
    path = []

    for n in unvisited_nodes:
        shortest_distance[n] = inf
    shortest_distance[start] = 0

    while unvisited_nodes:
        min_node = None

        for node in unvisited_nodes:
            if min_node == None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        if min_node == finish:
            break

        relatives_nodes_weights = graph[min_node]
        for relative_node, relative_node_weight in relatives_nodes_weights.items():
            if relative_node not in unvisited_nodes:
                continue

            possible_relative_node_weight = shortest_distance[min_node] + h[relative_node] + relative_node_weight
            if possible_relative_node_weight < shortest_distance[relative_node]:
                shortest_distance[relative_node] = possible_relative_node_weight
                previous_node_in_path[relative_node] = min_node

        unvisited_nodes.remove(min_node)

    current_node = finish
    while current_node != start:
        path.append(current_node)
        current_node = previous_node_in_path[current_node]
    path.append(start)

    path.reverse()
    return path

print(djikstras(graph, 'b','e'))
print(a_star(graph, h, 'b','e'))