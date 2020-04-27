class SArray:
    def __init__(self, string):
        super().__init__()
        self.string = string
        self.__arr = []
        self.__buildSA()

    def __buildSA(self):
        suffixes = self.__getSuffixes()
        prev_index = {v: i for i, v in enumerate(suffixes)}
        self.__sortSuffixes(suffixes)
        self.index_val = {}
        for val in suffixes:
            index = prev_index.get(val)
            self.__arr.append(index)
            self.index_val[index] = val

    def __getSuffixes(self):
        out = []
        for i in range(0, len(self.string)):
            out.append(self.string[i:])
        return out

    def __sortSuffixes(self, suffixes):
        suffixes.sort()

    @property
    def array(self):
        return self.__arr


if __name__ == "__main__":
    # sa = S__Array("abracadabra")

    sa = SArray("banana")
    print(sa.array)
