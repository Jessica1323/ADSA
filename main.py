class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    # 插入操作
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # 如果值已存在，不执行插入

        # 更新节点的高度
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 计算平衡因子
        balance = self.get_balance(root)

        # 左左情况
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # 右右情况
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # 左右情况
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # 右左情况
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # 删除操作
    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        # 更新节点高度
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 计算平衡因子
        balance = self.get_balance(root)

        # 左左情况
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # 左右情况
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # 右右情况
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # 右左情况
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # 获取节点高度
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    # 获取平衡因子
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # 获取最小值节点
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    # 左旋转
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # 右旋转
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # 前序遍历
    def preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.key)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return result

    # 中序遍历
    def inorder_traversal(self, root):
        result = []
        if root:
            result = result + self.inorder_traversal(root.left)
            result.append(root.key)
            result = result + self.inorder_traversal(root.right)
        return result

    # 后序遍历
    def postorder_traversal(self, root):
        result = []
        if root:
            result = result + self.postorder_traversal(root.left)
            result = result + self.postorder_traversal(root.right)
            result.append(root.key)
        return result

# 主函数
def main():
    tree = AVLTree()
    root = None
    commands = input().split()

    # 处理所有的 A 和 D 命令
    for command in commands[:-1]:
        if command[0] == 'A':
            value = int(command[1:])
            root = tree.insert(root, value)
        elif command[0] == 'D':
            value = int(command[1:])
            root = tree.delete(root, value)

    # 处理最后一个遍历命令
    traversal_command = commands[-1]
    if traversal_command == "PRE":
        result = tree.preorder_traversal(root)
    elif traversal_command == "POST":
        result = tree.postorder_traversal(root)
    elif traversal_command == "IN":
        result = tree.inorder_traversal(root)

    if result:
        print(" ".join(map(str, result)))
    else:
        print("EMPTY")

if __name__ == "__main__":
    main()
