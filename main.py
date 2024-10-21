class Node:
    def __init__(self, links, build_cost, destroy_cost):
        self.distance = 0  # 初始距离为0，用于Jarnik-Prim算法
        self.links = links  # 存储节点之间的道路
        self.build_cost = build_cost  # 建造成本
        self.destroy_cost = destroy_cost  # 破坏成本

    # 获取和设置函数
    def get_distance(self):
        return self.distance

    def set_distance(self, new_distance):
        self.distance = new_distance

    def get_links(self):
        return self.links

    def set_links(self, new_links):
        self.links = new_links

    def get_build_costs(self):
        return self.build_cost

    def set_build_costs(self, new_build_costs):
        self.build_cost = new_build_costs

    def get_destroy_costs(self):
        return self.destroy_cost

    def set_destroy_costs(self, new_destroy_costs):
        self.destroy_cost = new_destroy_costs


class Map:
    def __init__(self, new_nodes):
        self.nodes = new_nodes
        self.running_cost = 0

    def connect_nodes(self):
        print("")
        if len(self.nodes) == 1:
            self.running_cost = 0
            return

        new_nodes = self.nodes[:]
        curr_node = self.nodes[0]
        the_map = [curr_node]
        self.nodes[0] = None
        min_build_cost = 53
        map_indexer = 0
        link_existed = 0
        min_node = None
        parent_node = None
        index = -1

        while curr_node is not None:
            for i in range(len(curr_node.get_links())):
                if curr_node.get_links()[i] == '1':
                    if self.nodes[i] is not None:
                        the_map.append(self.nodes[i])
                        self.nodes[i] = None
                        link_existed = 1
                elif curr_node.get_links()[i] == '0' and self.nodes[i] is not None:
                    cost = curr_node.get_build_costs()[i]
                    cost_ascii = ord(cost) - 65 if ord(cost) <= 90 else ord(cost) - 71
                    if cost_ascii < min_build_cost:
                        min_build_cost = cost_ascii
                        min_node = self.nodes[i]
                        parent_node = curr_node
                        index = i

            if link_existed == 0 and len(the_map) == map_indexer + 1:
                the_map.append(min_node)
                self.nodes[index] = None
                new_link = list(parent_node.get_links())
                new_link[index] = '1'
                parent_node.set_links(''.join(new_link))

                new_link = list(min_node.get_links())
                for i in range(len(new_nodes)):
                    if parent_node.get_build_costs() == new_nodes[i].get_build_costs():
                        index = i

                new_link[index] = '1'
                min_node.set_links(''.join(new_link))
                map_indexer = 0
                link_existed = 0
                self.running_cost += min_build_cost
                min_build_cost = 53
            elif link_existed == 0 and len(the_map) > map_indexer + 1:
                map_indexer += 1
                curr_node = the_map[map_indexer]
                continue
            elif link_existed == 1:
                map_indexer = 0
                min_build_cost = 53
                link_existed = 0

            finished = all(node is None for node in self.nodes)
            if finished:
                curr_node = None
            else:
                parent_node = None
                curr_node = the_map[map_indexer]

        self.nodes = new_nodes

    def delete_roads(self):
        if len(self.nodes) == 1:
            self.running_cost = 0
            return

        curr_node = self.nodes[0]
        max_dest_cost = 0
        final_dest_cost = 0
        priority_queue = [curr_node]

        while curr_node is not None:
            if curr_node.get_distance() != 53:
                max_dest_cost += curr_node.get_distance()

            priority_queue.pop()
            curr_node.set_distance(53)

            for i in range(len(curr_node.get_links())):
                if curr_node.get_links()[i] == '1':
                    dest_cost = curr_node.get_destroy_costs()[i]
                    cost_ascii = ord(dest_cost) - 65 if ord(dest_cost) <= 90 else ord(dest_cost) - 71
                    if cost_ascii > self.nodes[i].get_distance() or (cost_ascii == 0 and self.nodes[i].get_distance() == 0):
                        self.nodes[i].set_distance(cost_ascii)
                        final_dest_cost += self.nodes[i].get_distance()

                        priority_queue = [node for node in priority_queue if node.get_build_costs() != self.nodes[i].get_build_costs()]
                        inserted = False
                        for j, node in enumerate(priority_queue):
                            if self.nodes[i].get_distance() < node.get_distance():
                                priority_queue.insert(j, self.nodes[i])
                                inserted = True
                                break
                        if not inserted:
                            priority_queue.append(self.nodes[i])
                    elif cost_ascii < self.nodes[i].get_distance() and self.nodes[i].get_distance() != 53:
                        final_dest_cost += cost_ascii

            if not priority_queue:
                curr_node = None
            else:
                curr_node = priority_queue[-1]

        self.running_cost += final_dest_cost - max_dest_cost

    def print_cost(self):
        print(self.running_cost)


def main():
    print("111")
    # 读取输入
    input_line = input().strip()
    tokens = input_line.split(',')
    
    build_line = input().strip()
    build = build_line.split(',')

    destroy_line = input().strip()
    destroy = destroy_line.split(',')

    # 创建节点列表
    nodes = [Node(tokens[i], build[i], destroy[i]) for i in range(len(tokens))]

    # 创建地图并执行操作
    my_map = Map(nodes)
    my_map.connect_nodes()
    my_map.delete_roads()
    my_map.print_cost()
    



main()
