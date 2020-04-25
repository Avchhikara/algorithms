"""This stack can be increasing as well as decreasing.
Some of the interesting problems related to this stack are:
Basic problem: https://leetcode.com/problems/Next-Greater-Element-II/
https://leetcode.com/problems/sum-of-subarray-minimums/ (High level)
it's explaination and other such problems link: 
https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
"""


def minc(arr):
    """Creates a monotonous increasing stack
        Shows the solutions for this problem: https://medium.com/@vishnuvardhan623/monotonic-stack-e9dcc4fa8c3e
    Arguments:
        arr {List[int]} -- array
    """
    stack = []
    for i in arr:
        while len(stack) and stack[-1] <= i:
            stack.pop()
        stack.append(i)
    return stack


print(minc([6, 5, 4, 3, 4, 6, 4, 3]))
