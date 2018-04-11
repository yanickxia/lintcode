# -*- coding:utf-8 -*-

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        F = [0] * (m + 1)
        for i in range(0, len(A)):
            for v in range(m, A[i] - 1, -1):
                F[v] = max(F[v], F[v - A[i]] + A[i])
        return F[-1]


s = Solution()
print(s.backPack(11, [2, 3, 5, 7]))
print(s.backPack(12, [2, 3, 5, 7]))
print(s.backPack(5000,
                 [828, 125, 740, 724, 983, 321, 773, 678, 841, 842, 875, 377, 674, 144, 340, 467, 625, 916, 463, 922,
                  255, 662, 692, 123, 778, 766, 254, 559, 480, 483, 904, 60, 305, 966, 872, 935, 626, 691, 832, 998,
                  508, 657, 215, 162, 858, 179, 869, 674, 452, 158, 520, 138, 847, 452, 764, 995, 600, 568, 92, 496,
                  533, 404, 186, 345, 304, 420, 181, 73, 547, 281, 374, 376, 454, 438, 553, 929, 140, 298, 451, 674, 91,
                  531, 685, 862, 446, 262, 477, 573, 627, 624, 814, 103, 294, 388]
                 ))
