"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 18:10 13.11.2020

This was already done while I was doing BinaryTree Questions in Java. This is the Python version of that.
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        output = root  # Save the head

        if root is None: return None

        while (root.left != None):
            next_most_left = root.left  # Save for the next loop

            while (root != None):
                root.left.next = root.right
                root.right.next = root.next.left if root.next != None else None
                root = root.next

            root = next_most_left

        return output
