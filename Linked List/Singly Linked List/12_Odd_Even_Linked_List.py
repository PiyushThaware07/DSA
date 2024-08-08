'''
Odd Even Linked List ~> You are Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
'''
from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def oddEvenList(self,myList):
        head = myList.head
        odd_dummy = CreateNode(-1)
        even_dummy = CreateNode(-1)
        odd = odd_dummy
        even = even_dummy
        index = 0

        while head is not None:
            if index % 2 == 0:
                even.next = CreateNode(head.data)
                even = even.next
            else:
                odd.next = CreateNode(head.data)
                odd = odd.next
            index = index + 1
            head = head.next
        even.next = odd_dummy.next
        myList.head = even_dummy.next
        myList.traversal()
        





ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)
ll1.traversal()

s = Solution()
s.oddEvenList(ll1)
