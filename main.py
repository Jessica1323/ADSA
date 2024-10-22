def letter_to_cost(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    else:
        raise ValueError(f"Invalid: {c}")

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if xroot == yroot:
        return  
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def minimal_cost(country_str, build_str, destroy_str):
    country_rows = country_str.strip().split(',')
    build_rows = build_str.strip().split(',')
    destroy_rows = destroy_str.strip().split(',')
    
    n = len(country_rows)
    
    if not (all(len(row) == n for row in country_rows) and
            all(len(row) == n for row in build_rows) and
            all(len(row) == n for row in destroy_rows)):
        raise ValueError("All input matrices must be square and of the same size.")
    
    total_destroy_cost = 0
    for i in range(n):
        for j in range(n):
            if i < j and country_rows[i][j] == '1':
                destroy_cost = letter_to_cost(destroy_rows[i][j])
                total_destroy_cost += destroy_cost
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if country_rows[i][j] == '1':
                destroy_cost = letter_to_cost(destroy_rows[i][j])
                edge_cost = -destroy_cost
                edges.append((edge_cost, i, j))
            else:
                build_cost = letter_to_cost(build_rows[i][j])
                edge_cost = build_cost
                edges.append((edge_cost, i, j))
    
    edges.sort()
    

    parent = [i for i in range(n)]
    rank = [0] * n
    
    mst_cost = 0
    edges_used = 0  
    
    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break  
    
    if edges_used != n - 1:
        raise ValueError("It's impossible to connect all cities into a tree.")

    minimal_total_cost = total_destroy_cost + mst_cost
    
    return minimal_total_cost


if __name__ == "__main__":
    str = input()
    nextStr = str.split(" ")
    print(nextStr)
    output1 = minimal_cost(nextStr[0],nextStr[1],nextStr[2])
    print(output1)  
