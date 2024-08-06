'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example :
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''
from custom.linkedlist import LinkedList,CreateNode

class Solution:
    def brute(self,myList,target):
        length = 0
        l1 = myList.head
        while l1 is not None:
            length += 1
            l1 = l1.next 

        i = 1
        l2 = myList.head
        while i < length - target:
            l2 = l2.next 
            i = i + 1
        l2.next = l2.next.next 
        myList.traversal()

        



            



ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)

# ll1.addEnd(1)
# ll1.addEnd(2)
ll1.traversal()

s = Solution()
s.brute(ll1,1)