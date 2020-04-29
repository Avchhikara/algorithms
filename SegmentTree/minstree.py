class MinSegmentTree:
    def __init__(self, arr):
        super().__init__()
        self.__arr = arr
        self.__construct()

    def __construct(self):
        arr = self.__arr
        l = len(arr)
        new_len = self.__getPowerOfTwo(l)*2
        self.__tree = tree = [float('inf')]*new_len
        # print(tree)
        self.__buildTree(tree, 0, l-1, 0)
        # print(tree)

    def __buildTree(self, tree, low, high, curr):
        if low == high:
            tree[curr] = self.__arr[low]
            return
        mid = (low + high) // 2
        self.__buildTree(tree, low, mid, 2*curr + 1)
        self.__buildTree(tree, mid + 1, high, 2*curr + 2)
        tree[curr] = min(tree[2*curr + 1], tree[2*curr + 2])

    def minRangeQuery(self, start, end):
        return self.__getMin(start, end, 0, len(self.__tree))

    def __getMin(self, qlow, qhigh, low, high, pos=0):
        # print(pos, low, high)
        if qlow <= low and qhigh >= high:
            return self.__tree[pos]
        if qlow > high or qhigh < low:
            return float('inf')
        mid = (low + high)//2
        return min(self.__getMin(qlow, qhigh, low, mid, 2*pos + 1), self.__getMin(qlow, qhigh, mid + 1, high, 2*pos + 2))

    def __getPowerOfTwo(self, num):
        i = 1
        while 2**i < num:
            i += 1
        return 2**i

        # 0, 1, 2, 3, 4, 5
        #-1, 3, 4 | 0, 2, 1
        #-1, 3 | 4
        #-1 | 3
st1 = MinSegmentTree([-1, 3, 4, 0, 2, 1])
st2 = MinSegmentTree([-1, 0, 3, 6])

print(st1.minRangeQuery(2, 4))
