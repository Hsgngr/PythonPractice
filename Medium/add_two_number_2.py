"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 22:34 8.11.2020

https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3522/

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr_1 = []
        arr_2 = []

        while l1 != None:
            arr_1.append(l1.val)

            l1 = l1.next
        while l2 != None:
            arr_2.append(l2.val)

            l2 = l2.next

        sum_1 = 0
        sum_2 = 0
        for i in range(len(arr_1)):
            sum_1 += arr_1[i] * 10 ** (len(arr_1) - i - 1)

        for i in range(len(arr_2)):
            sum_2 += arr_2[i] * 10 ** (len(arr_2) - i - 1)

        s3 = sum_1 + sum_2
        print(s3)
        tail = None;
        head = None

        while s3 > 0:
            head = ListNode(s3 % 10)
            head.next = tail
            tail = head
            s3 /= 10

        if head:
            return head
        else:
            return ListNode(0)


'''
Cleaner Solution:
https://leetcode.com/problems/add-two-numbers-ii/discuss/202769/Fast-simple-Python

class Solution(object):
    def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		# turn the lists in to ints with simple loops. In case you didn't know, you can put
		# multiple statements on the same line if you use semicolons in Python.
		s1 = 0
		s2 = 0
		while l1: s1 *= 10; s1 += l1.val; l1 = l1.next
		while l2: s2 *= 10; s2 += l2.val; l2 = l2.next

		# take the sum and reconstruct the number from tail to head, because it's easier
		# to isolate and chop off the little digits with modulus and division.
		s3 = s1 + s2
		tail = None
		head = None
		while s3 > 0: head = ListNode(s3 % 10); head.next = tail; tail = head; s3 /= 10
		return head if head else ListNode(0)

'''
