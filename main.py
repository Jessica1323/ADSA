class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    # 省略插入函数

    def delete(self, root, key):
        # 改进的删除方法（已更新）

    # 左旋，右旋，以及辅助函数（省略）
     def preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.key)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return result

    def inorder_traversal(self, root):
        result = []
        if root:
            result = result + self.inorder_traversal(root.left)
            result.append(root.key)
            result = result + self.inorder_traversal(root.right)
        return result

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
