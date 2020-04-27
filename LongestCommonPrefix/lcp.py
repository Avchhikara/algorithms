from suffixarray import SArray


class LCP:
    def __init__(self, string):
        super().__init__()
        self.__lcp = []
        self.__buildLCP(string)

    def __buildLCP(self, string):
        self.__sarr = SArray(string).array
