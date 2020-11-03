"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 13:11 11.10.2020
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'Node : ' + str(self.val)


def insertion_sortlist(head):
    if head == None: return head
    if head.next == None:
        return head
    current_node = head
    min_node = current_node
    output_node = ListNode()
    last_output_node = output_node

    while current_node != None:
        min_node = current_node
        prev_node = ListNode(None)
        min_left_node = prev_node
        while current_node != None:

            # Find the minimum node
            if current_node.val < min_node.val:
                min_node = current_node
                if prev_node != None:
                    min_left_node = prev_node

            if current_node.next != None:
                prev_node = current_node

            current_node = current_node.next
        # Remove the minimum node
        # print(printAllList(head))
        if min_left_node.val != None:
            min_left_node.next = min_node.next
        else:
            head = min_node.next

        last_output_node.next = min_node
        last_output_node = last_output_node.next
        last_output_node.next = None

        # print(printAllList(head))

        if head.next == None:
            last_output_node.next = head
            break
        else:
            current_node = head

    return output_node.next


def printAllList(head):
    list = []
    while head != None:
        list.append(head.val)
        head = head.next

    return list


if __name__ == '__main__':
    # a = ListNode(4)
    # b = ListNode(2)
    # c = ListNode(1)
    # d = ListNode(3)
    # a.next = b
    # b.next = c
    # c.next = d

    a = ListNode(-1)
    b = ListNode(5)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(0)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    result = insertion_sortlist(a)
    print(printAllList(result))

# Someone has a better idea:
# https://leetcode.com/problems/insertion-sort-list/discuss/46420/An-easy-and-clear-way-to-sort-(-O(1)-space-)