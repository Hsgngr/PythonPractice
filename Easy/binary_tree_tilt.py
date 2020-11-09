"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 02:56 9.11.2020
LeetCode November Challenge Sunday
https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3524/

To be honest, I couldnt do it %100 here is the answer:
https://leetcode.com/problems/binary-tree-tilt/discuss/102321/Python-Simple-with-Explanation
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node : ' + str(self.val)


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def _sum(node):
            if not node: return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right

        _sum(root)

        return self.ans


if __name__ == '__main__':
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(9)
    d = TreeNode(3)
    e = TreeNode(5)
    f = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    sol = Solution()
    print(sol.findTilt(a))
