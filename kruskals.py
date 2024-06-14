def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal_mst(graph, V):
    result = []
    graph = sorted(graph, key=lambda item: item[2])
    parent = [i for i in range(V)]
    rank = [0] * V
    e = 0
    i = 0
    while e < V - 1:
        u, v, w = graph[i]
        i += 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)
        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    return result

graph = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
]
V = 4

mst = kruskal_mst(graph, V)
print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")
