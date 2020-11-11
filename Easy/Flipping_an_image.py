"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 00:10 11.11.2020
"""


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range(len(row) // 2):
                temp_val = row[i]
                row[i] = row[len(row) - i - 1]
                row[len(row) - i - 1] = temp_val

            for i in range(len(row)):
                row[i] = 1 if row[i] == 0 else 0

        return A


if __name__ == '__main__':
    sol = Solution()

    arr = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

    print(sol.flipAndInvertImage(arr))
