class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class LCA:
    def __init__(self, tree):
        l = len(tree)*2
        self.__nodes = []
        self.__depth = []
        self.__last = [0]*len(tree)
        self.__tree = tree
        self.__construct()

    def __construct(self):
        self.__dfs(0, len(), 0, 0)
        print(self.__depth, self.__nodes)

    def __dfs(self, low, high, pos, depth):
        if low <= high and pos <= high:
            self.__depth.append(depth)
            self.__nodes.append(pos)
            left = self.__dfs(low, high, 2*pos + 1, depth + 1)
            right = self.__dfs(low, high, 2*pos + 2, depth + 1)
            self.__depth.append(depth)
            self.__nodes.append(pos)
