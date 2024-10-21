def letter_to_cost(letter):
    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A')
    elif 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 26
    else:
        return float('inf')

def parse_input(input_string):
    parts = input_string.strip().split(' ')
    country_str, build_str, destroy_str = parts[0], parts[1], parts[2]
    
    country = [list(map(int, row)) for row in country_str.split(',')]
    build = [list(row) for row in build_str.split(',')]
    destroy = [list(row) for row in destroy_str.split(',')]
    
    return country, build, destroy

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return False

        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1

        return True

def kruskal(n, country, build, destroy):
    uf = UnionFind(n)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == 1:
                cost = letter_to_cost(destroy[i][j])
                edges.append((i, j, cost, 'destroy'))
            else:
                cost = letter_to_cost(build[i][j])
                edges.append((i, j, cost, 'build'))

    edges = sorted(edges, key=lambda x: x[2])

    mst_weight = 0
    connected_components = n

    for u, v, weight, action in edges:
        if uf.union(u, v):
            mst_weight += weight
            connected_components -= 1

    if connected_components > 1:
        return float('inf')
    
    return mst_weight

def process_input():
    input_string = input()
    country, build, destroy = parse_input(input_string)
    n = len(country)

    mst_weight = kruskal(n, country, build, destroy)

    print(f"{mst_weight}")

process_input()
