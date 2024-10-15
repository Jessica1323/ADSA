class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1


def char_to_cost(c):
    cost_map = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
        'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35,
        'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45,
        'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51
    }
    
    return cost_map.get(c, float('inf')) 


def min_cost_reconstruction(n, country, build, destroy):
    edges = []
    
    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':  
                destroy_cost = char_to_cost(destroy[i][j])
                edges.append((destroy_cost, i, j, "destroy"))
            if country[i][j] == '0':  
                build_cost = char_to_cost(build[i][j])
                edges.append((build_cost, i, j, "build"))
    
    edges.sort()
    
    uf = UnionFind(n)
    total_cost = 0
    
    for cost, u, v, action in edges:
        if uf.find(u) != uf.find(v): 
            uf.union(u, v)
            total_cost += cost
            if action == "destroy":
                print(f"Destroying road between {u} and {v}, cost: {cost}")
            elif action == "build":
                print(f"Building road between {u} and {v}, cost: {cost}")
    
    return total_cost

n = 3
country = ["011", "101", "110"]
build = ["ABD", "BAC", "DCA"]
destroy = ["ABD", "BAC", "DCA"]

result = min_cost_reconstruction(n, country, build, destroy)
print(result) 