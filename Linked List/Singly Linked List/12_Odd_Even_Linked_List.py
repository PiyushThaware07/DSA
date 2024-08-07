'''
Odd Even Linked List ~> You are Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
'''
from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def oddEvenList(self,myList):
        pass 


ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)
ll1.traversal()

s = Solution()
s.oddEvenList(ll1)
