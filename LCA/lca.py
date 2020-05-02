class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __str__(self):
        return f"Value: {self.val}, with children: {self.children}"


class LCA:
    def __init__(self, tree):
        self.__nodes = []
        self.__depth = []
        self.__tree = tree
        self.__construct()

    def __construct(self):
        self.__dfs(self.__tree, 0)
        print(self.__depth, self.__nodes)

    def __dfs(self, node, depth):
        if node:
            self.__depth.append(depth)
            self.__nodes.append(node.val)
            for child in node.children:
                self.__dfs(child, depth + 1)
                self.__depth.append(depth)
                self.__nodes.append(node.val)


tree = Node(0)
tree.children.append(Node(1))
tree.children[0].children.append(Node(3))
tree.children.append(Node(2))
tree.children[1].children.append(Node(4))
tree.children[1].children[0].children.append(Node(5))
print(tree)
lca = LCA(tree)
