# -*- coding:utf-8 -*-

class Solution:
    """
    @param prices: the prices
    @param n: the length of rod
    @return: the max value
    """

    def cutting(self, prices, n):
        F = [0] * (n + 1)
        for i in range(0, len(prices)):
            for v in range(i + 1, n + 1):
                F[v] = max(F[v], F[v - i - 1] + prices[i])
        return F[-1]


s = Solution()
print(s.cutting([1, 5, 8, 9, 10, 17, 17, 20], 8))
print(s.cutting([3, 5, 8, 9, 10, 17, 17, 20], 8))
print(s.cutting([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 25))
