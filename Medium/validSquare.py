"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 22:41 11.11.2020
"""
import math


class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1 == p2 == p3 == p4: return False

        def dist(x1, x2):
            return round(math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2), 4)

        ls = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        ls.sort()

        if ls[0] == ls[1] == ls[2] == ls[3] and ls[4] == ls[5]:
            return True

        else:
            False

            
# class Solution(object):
#
#     def validSquare(self, p1, p2, p3, p4):
#         """
#         :type p1: List[int]
#         :type p2: List[int]
#         :type p3: List[int]
#         :type p4: List[int]
#         :rtype: bool
#         """
#         import math
#         # Anchor point p1
#         p1_2 = self.distance(p1, p2)
#         p1_3 = self.distance(p1, p3)
#         p1_4 = self.distance(p1, p4)
#         print('p1_2', p1_2)
#         print('p1_3', p1_3)
#         print('p1_4', p1_4)
#         if p1_2 == p1_3:
#             # Check if p1_4= p1_2 * sqrt(2)
#             if p1_4 == round(p1_2 * math.sqrt(2), 4):
#                 p4_2 = self.distance(p4, p2)
#                 p4_3 = self.distance(p4, p3)
#                 if p4_2 == p4_3:
#                     return True
#
#         elif p1_2 == p1_4:
#
#             if p1_3 == round(p1_2 * math.sqrt(2), 4):
#                 p3_2 = self.distance(p3, p2)
#                 p3_4 = self.distance(p3, p4)
#                 if p3_2 == p3_4:
#                     return True
#
#         elif p1_3 == p1_4:
#             print('p1_3 == p1_4')
#             print('p1_2:', p1_2)
#             print('p1_3', p1_3)
#             print('p1_3sqrt2:', round(p1_3 * math.sqrt(2)))
#             if p1_2 == round(p1_3 * math.sqrt(2), 4):
#                 p2_3 = self.distance(p2, p3)
#                 p2_4 = self.distance(p2, p4)
#                 if p2_3 == p2_4:
#                     return True
#         else:
#             return False
#
#     def distance(self, x1, x2):
#         return round(math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2), 4)


if __name__ == '__main__':
    sol = Solution()

    p1 = [1134, -2539]
    p2 = [492, -1255]
    p3 = [-792, -1897]
    p4 = [-150, 3181]

    print(sol.validSquare(p1, p2, p3, p4))
