# -*- coding:utf-8 -*-

class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        tmpList = [1, 1]
        for i in range(0, n - 1):
            x = tmpList[-1] + tmpList[-2]
            tmpList.append(x)
        return tmpList[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
