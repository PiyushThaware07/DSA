'''
PROBLEM STATEMENT : Starting point of loop in a Linked List
Given the head of a linked list that may contain a cycle, 
return the starting point of that cycle. 
If there is no cycle in the linked list return null.
'''

from custom.linkedlist import LinkedList

class Solution:
    def better(self, myList):
        head = myList.head
        hashMap = {}
        while head:
            if head in hashMap:
                print(head.data)
                return
            else:
                hashMap[head] = 1
            head = head.next
        print("no cycle")
    
    def optimize(self,myList):
        head = myList.head
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                print(slow)
                return
        print("No cycle")
        return
        
            
            
        


# Creating the linked list
myList = LinkedList()
myList.addEnd(101)
myList.addEnd(102)
myList.addEnd(103)
myList.addEnd(104)
myList.addEnd(105)

# Detect the cycle and find the start of the cycle
sol = Solution()

# CREATE CYCLE (manually)
current = myList.head
cycle_start = None
while current.next:
    if current.data == 103:
        cycle_start = current  # Node where cycle starts
    current = current.next
current.next = cycle_start
sol.optimize(myList)