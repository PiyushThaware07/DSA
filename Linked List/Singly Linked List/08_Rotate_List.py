'''
1 -> 2 -> 3 -> 4 -> 5
k = 2 
5 -> 4 -> 3 -> 2 -> 1
'''
from requests import head
from custom.linkedlist import LinkedList
class Solution:
    def optimize(self,myList,k):
        head1 = myList.head    # 1 -> 2 -> 3 -> 4 -> 5 -> null
        length = 1
        while head1.next is not None:
            length += 1
            head1 = head1.next 
        head1.next = myList.head

        k = k % length
        if k == 0:
            head1.next = None  # Break the circular link
            myList.traversal()
            return

        split = length - k 
        head2 = head1.next
        for i in range(0,split-1):
            head2 = head2.next 
        myList.head = head2.next
        head2.next = None
        myList.traversal()
        return 





ll1 = LinkedList()
# ll1.addEnd(101)
# ll1.addEnd(202)
# ll1.addEnd(303)
# ll1.addEnd(404)
# ll1.addEnd(505)

ll1.addEnd(0)
ll1.addEnd(1)
ll1.addEnd(2)
ll1.traversal()
s = Solution()
s.optimize(ll1,4)
