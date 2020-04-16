"""
给出两个非空的链表用来表示两个非负的整数。其中，它们格子的位数是按照逆序的方式存储的，
并且它们的每个节点只能存储一位数字。
如果，我们江这两个数相加起来，则会返回一个新的链表来表示它们的和。
除0以外，没有数以0开头。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    链表基础
    """
    target = ListNode(1)
    p = target
    flag = 0
    while l1 and l2:
        p.next = ListNode((l1.val + l2.val + flag) % 10)
        flag = (l1.val + l2.val + flag) // 10
        p, l1, l2 = p.next, l1.next, l2.next
    l1 = l1 if l1 else l2
    while flag:
        if l1:
            p.next = ListNode((l1.val + flag) % 10)
            flag = (l1.val + flag) // 10
            p, l1 = p.next, l1.next
        else:
            p.next = ListNode(flag)
            p = p.next
            break
    p.next = l1

    return target.next


def addTwoNumbers2(l1, l2):
    target = ListNode(1)
    dummy = target
    flag = 0
    while l1 and l2:
        dummy.next = ListNode((l1.val + l2.val + flag) % 10)
        flag = (l1.val + l2.val + flag) // 10
        dummy, l1, l2 = dummy.next, l1.next, l2.next
    l1 = l1 if l1 else l2
    while flag:
        if l1:
            dummy.next = ListNode((l1.val + flag) % 10)
            flag = (l1.val + flag) // 10
            dummy, l1 = dummy.next, l1.next
        else:
            dummy.next = ListNode(flag)
            dummy = dummy.next
            break
    dummy.next = l1

    return target.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = addTwoNumbers2(l1, l2)
    res = []
    while result:
        res.append(result.val)
        result = result.next
    print(res)
