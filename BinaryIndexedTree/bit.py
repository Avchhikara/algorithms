from typing import List


class BIT:
    def __init__(self, arr):
        super().__init__()
        self.arr = arr
        self.__bit = [0]*(len(arr) + 1)
        self.__create()

    def __create(self):
        for i, v in enumerate(self.arr):
            self.__updateBIT(i, v)

    def __updateBIT(self, index, val):
        index += 1
        while index <= len(self.__bit):
            self.__bit[index] += val
            index += self.__getParent(index)

    def __getParent(self, index):
        """gives us the last set bit for eg:
        index = 5 = 0101
        it will return = 1
        other eg: index = 10 = 1010
        it will return 10

        Arguments:
            index {int} -- current index

        Returns:
            int -- last set bit
        """
        return index & (-index)

    def getSum(self, x, y=-1):
        """return the sum from x(excluding) to y(including)

        Arguments:
            x {int} -- starting index

        Keyword Arguments:
            y {int} -- ending index (including) (default: {-1})

        Returns:
            int -- sum from x(excluding) to y (including)
        """
        y, x = min(x, y), max(x, y)
        return self.__getSum(x) - self.__getSum(y)

    def __getSum(self, index):
        """this will just get the sum from 0 to index (including)
        Arguments:
            index {int} -- index (including) upto which the sum is needed from 0 
        """
        s = 0
        index += 1
        while index > 0:
            s += self.__bit[index]
            index -= self.__getParent(index)
        return s

    def update(self, index, val):
        """update the value in the array

        Arguments:
            index {int} -- index to be updated
            val {int} -- value to be added to the index
        """
        self.__updateBIT(index, val)


bit = BIT([2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9])
print(bit.getSum(5, 10))
