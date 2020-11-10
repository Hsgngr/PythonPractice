"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 00:15 10.11.2020
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
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find_min_max(node, min_val, max_val):
            if not node: return max_val - min_val

            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)

            return max(find_min_max(node.left, min_val, max_val), find_min_max(node.right, min_val, max_val))

        return find_min_max(root, 1000000, 0)


if __name__ == '__main__':
    a = TreeNode(8)
    b = TreeNode(3)
    c = TreeNode(1)
    d = TreeNode(6)
    e = TreeNode(4)
    f = TreeNode(7)
    g = TreeNode(10)
    h = TreeNode(14)
    i = TreeNode(13)

    a.left = b
    a.right = g
    b.left = c
    b.right = d
    d.left = e
    d.right = f
    g.right = h
    h.left = i

    sol = Solution()
    print(sol.maxAncestorDiff(a))
