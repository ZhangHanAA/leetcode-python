# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    result = sol.addTwoNumbers(l1,l2)
    res = []
    while result:
        res.append(result.val)
        result = result.next
    print(res)