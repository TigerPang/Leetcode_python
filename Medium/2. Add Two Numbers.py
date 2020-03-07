# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        total = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 != None and l2 != None:
            total = l1.val + l2.val + carry
            carry = total // 10
            temp = ListNode(total % 10)
            curr.next = temp
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            total = l1.val + carry
            carry = total // 10
            temp = ListNode(total % 10)
            curr.next = temp
            curr = curr.next
            l1 = l1.next
        while l2 != None:
            total = l2.val + carry
            carry = total // 10
            temp = ListNode(total % 10)
            curr.next = temp
            curr = curr.next
            l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy.next

def stringToIntegerList(input):
    L = []
    for i in input:
        L.append(int(i))
    return L

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():

    l1 = stringToListNode("2345678");
    l2 = stringToListNode("5645678");
    ret = Solution().addTwoNumbers(l1, l2)
    out = listNodeToString(ret);
    print(out)


if __name__ == '__main__':
    main()
