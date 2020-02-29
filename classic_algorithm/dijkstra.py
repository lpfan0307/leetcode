def dijkstra(graph, src):
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]
    visited = []
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance = {src:0}
    path={src:{src:[]}}
    k = pre = src
    while nodes:
        mid_distance = float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v] + graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance
                    k = d
                    pre = v
        distance[k] = mid_distance
        path[src][k] = [i for i in path[src][pre]]
        path[src][k].append(k)
        visited.append(k)
        nodes.remove(k)
    return distance, path

if __name__ == '__main__':
    graph_list = [ [0, 2, 1, 4, 5, 1],
            [1, 0, 4, 2, 3, 4],
            [2, 1, 0, 1, 2, 4],
            [3, 5, 2, 0, 3, 3],
            [2, 4, 3, 4, 0, 1],
            [3, 4, 7, 3, 1, 0]]

    distance,path= dijkstra(graph_list, 0)  
    print(distance,path)
                       