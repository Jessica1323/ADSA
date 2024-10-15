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
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    return float('inf')  

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
    
    return total_cost

n = 3
country = ["011", "101", "110"]
build = ["ABD", "BAC", "DCA"]
destroy = ["ABD", "BAC", "DCA"]

result = min_cost_reconstruction(n, country, build, destroy)
print(result)
