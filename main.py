# 定义字母到数字的转换函数
def letter_to_cost(letter):
    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A')  # 'A' 对应 0, ..., 'Z' 对应 25
    elif 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 26  # 'a' 对应 26, ..., 'z' 对应 51
    else:
        return float('inf')  # 如果不是有效字符，返回无穷大表示不能使用的路径

# 解析输入字符串为矩阵
def parse_input(input_string):
    parts = input_string.strip().split(' ')
    country_str, build_str, destroy_str = parts[0], parts[1], parts[2]
    
    # 将字符串转化为二维矩阵
    country = [list(map(int, row)) for row in country_str.split(',')]
    build = [list(row) for row in build_str.split(',')]
    destroy = [list(row) for row in destroy_str.split(',')]
    
    return country, build, destroy

# 定义并查集数据结构
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # 找到节点的根，并进行路径压缩
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    # 合并两个节点所在的集合
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return False

        # 合并时将rank低的树接到rank高的树上
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1

        return True

# Kruskal算法：找到最小生成树的路径
def kruskal(n, country, build, destroy):
    # 初始化并查集
    uf = UnionFind(n)

    # 构建所有边的信息，包含建造成本或销毁成本
    edges = []

    for i in range(n):
        for j in range(i + 1, n):  # 只遍历上三角矩阵，避免重复计算无向边
            if country[i][j] == 1:
                # 如果已经存在道路，销毁的成本
                cost = letter_to_cost(destroy[i][j])
                edges.append((i, j, cost, 'destroy'))
            else:
                # 如果不存在道路，建造的成本
                cost = letter_to_cost(build[i][j])
                edges.append((i, j, cost, 'build'))

    # 按边的权重从小到大排序
    edges = sorted(edges, key=lambda x: x[2])

    mst_weight = 0  # 最小生成树的总权重
    connected_components = n  # 连通分量数

    # 遍历每条边，选择不会形成环的边
    for u, v, weight, action in edges:
        if uf.union(u, v):  # 如果这条边不形成环
            mst_weight += weight
            connected_components -= 1

    return mst_weight, connected_components

# 示例输入处理
def process_input(input_string):
    country, build, destroy = parse_input(input_string)
    n = len(country)  # 城市数量

    mst_weight, connected_components = kruskal(n, country, build, destroy)

    # 输出最小生成树权重
    print(f"{mst_weight}")

# 示例输入
input_string = "011,101,110 ABD,BAC,DCA ABD,BAC,DCA"
process_input(input_string)
