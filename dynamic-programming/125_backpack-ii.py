# -*- coding:utf-8 -*-
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        F = [0] * (m + 1)
        for i in range(0, len(A)):
            for v in range(m, A[i] - 1, -1):
                F[v] = max(F[v], F[v - A[i]] + V[i])
        return F[-1]
