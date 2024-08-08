'''
Palindrome --> Reverse of a linked list is also similar as follows.

original => 1 -> 0 -> 0 -> 1 
reverse  => 1 -> 0 -> 0 -> 1
since original equals to reverse then it is a palindrome.
'''

from custom.linkedlist import CreateNode, LinkedList

class Solution:
    def isPalindrome(self,myList):
        head = myList.head
        result = []
        while head is not None:
            result.append(head.data)
            head = head.next
        reverse_result = result[::-1]
        print(reverse_result,result)
        if result == reverse_result:
            print("Palindrome")
        else:
            print("Not Palindrome")
        


ll1 = LinkedList()
ll1.addEnd(1)
ll1.addEnd(0)
ll1.addEnd(0)
ll1.addEnd(1)
ll1.traversal()

s = Solution()
s.isPalindrome(ll1)