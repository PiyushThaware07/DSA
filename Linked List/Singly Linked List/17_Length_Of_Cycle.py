from custom.linkedlist import LinkedList

class Solution:
    def better(self, myList):
        # Initialize a hashMap to store nodes and their first occurrence position
        hashMap = {}
        timer = 0  # This acts as a counter for the number of nodes visited (step/iteration)
        head = myList.head  # Start from the head of the linked list
        
        # Traverse the linked list to detect a cycle
        while head:
            timer += 1  # Increment the step as we visit a new node

            # If the node has already been visited, it means a cycle is present
            if head in hashMap:
                # Print the length of the cycle, which is the difference in the timer values
                print("Cycle Length:", timer - hashMap[head])
                return

            # Otherwise, record the node and the current step in the hashMap
            else:
                hashMap[head] = timer

            # Move to the next node in the list
            head = head.next
        
        # If no cycle is detected, print "No Cycle"
        print("No Cycle")
        return



    def optimize(self,myList):
        head = myList.head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:    # Cycle
                length = 0
                while slow != fast:
                    length += 1
                    fast = fast.next
                print(length)
                return
        print("No Cycle")
        return
    
    
myList = LinkedList()
myList.addEnd(101)
myList.addEnd(102)
myList.addEnd(103)
myList.addEnd(104)
myList.addEnd(105)

# Create a cycle manually by linking the last node to the node with data 103
current = myList.head
cycle_start = None
while current.next:
    if current.data == 104:
        cycle_start = current  # Identify the node where the cycle starts
    current = current.next
current.next = cycle_start  # Creating the cycle by connecting the last node to node 103

# Detect the cycle and find the cycle length (if any)
sol = Solution()
sol.better(myList)
