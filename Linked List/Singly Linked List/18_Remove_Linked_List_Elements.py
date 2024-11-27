'''
PROBLEM STATEMENT : Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1 : 
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2 :
Input: head = [7,7,7,7] val = 7
Output: []
'''
from custom.linkedlist import LinkedList
class Solution:
    def RemoveElements(self,myList,val):
        head = myList.head
        while head and head.data == val:
            head = head.next
            
        current = head
        # But it will check form the item-2 of a linked list but what about the first index element of linked list for that we have above code
        while current and current.next:
            if current.next.data == val:
                current.next = current.next.next
            else:
                current = current.next
        myList.head = head
        myList.traversal()


myList = LinkedList()
myList.addEnd(1)
myList.addEnd(2)
myList.addEnd(6)
myList.addEnd(3)
myList.addEnd(4)
myList.addEnd(5)
myList.addEnd(6)

sol = Solution()
sol.RemoveElements(myList,6)