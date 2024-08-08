from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def hasCycle(self,myList):
        head = myList.head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next        # Move slow pointer by 1 step 
            fast = fast.next.next   # Move fast pointer by 2 steps
            if slow == fast:        # If they meet, there's a cycle
                print("Cycle present")
                return
        print("Cycle not present")
        return


ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(2)
ll1.addEnd(3)
ll1.addEnd(4)
ll1.addEnd(5)
ll1.traversal()

s = Solution()
s.hasCycle(ll1)