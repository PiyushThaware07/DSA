from multiprocessing import dummy


class CreateNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        else:
            current = self.head
            while current is not None:
                print(current.data,end=" -> ")
                current = current.next
            print(None)
    
    def insertBegin(self,data):
        newNode = CreateNode(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertEnd(self,data):
        newNode = CreateNode(data)
        if self.head is None:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            
    
    def deleteNode(self,targetNode):
        if targetNode is None or targetNode.next is None:
            print("targetNode not found!")
            return
        else:
            targetNode.data = targetNode.next.data
            targetNode.next = targetNode.next.next
        
    
    def reverseLinkedList(self):
        if self.head is None:
            print("Linkedlist is empty!")
            return
        else:
            current = self.head
            previous = None
            while current is not None:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            self.head = previous
    
    def mergeTwoSorted(self,list1,list2):
        head1 = list1.head
        head2 = list2.head
        node = CreateNode(-1)
        dummy = node
        while head1 and head2:
            if head1.data < head2.data:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
        if head1 is not None:
            dummy.next = head1
        else:
            dummy.next = head2
        # traverse list
        mergedList = LinkedList()
        mergedList.head = node.next
        mergedList.traversal()
    
    
    def addTwoNumberInLinkedList(self,list1,list2):
        head1 = list1.head
        head2 = list2.head
        node = CreateNode(-1)
        dummy = node
        carry = 0
        
        while head1 or head2 or carry:
            data1 = head1.data if head1 is not None else 0
            data2 = head2.data if head2 is not None else 0
            
            sumbmission = data1+data2+carry
            remainder = sumbmission % 10
            carry = sumbmission // 10
            
            newNode = CreateNode(remainder)
            dummy.next = newNode
            dummy = dummy.next
            
            if head1 is not None:
                head1 = head1.next
            if head2 is not None:
                head2 = head2.next
        
        resultList = LinkedList()
        resultList.head = node.next
        resultList.traversal()
        
    
    def removeNthNodeFromEndOfLinkedList(self,myList,target):
        node = CreateNode(-1)
        dummy = node
        dummy.next = myList.head
        # ORIGINAL : 1->2->3->4->Null  => -1->1->2->3->4->Null
        slowPtr = dummy
        fastPtr = dummy
        for _ in range(target+1):
            if fastPtr is None:
                print("target value of deletion of node from end is more then as compared to actual element present in linked list")
                return
            fastPtr = fastPtr.next
        while fastPtr is not None:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        slowPtr.next = slowPtr.next.next
        myList.head = dummy.next
        myList.traversal()
        
    def middleOfLinkedList(self,myList):
        fastPtr = myList.head
        slowPtr = myList.head
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
        print(slowPtr.data)
        
    
    def swapAdjacentNodesInPair(self,myList):
        # 100 -> 200 -> 300
        node = CreateNode(-1)
        dummy = node
        dummy.next = myList.head
        current = dummy
        # -1 -> 100 -> 200 -> 300
        while current.next and current.next.next:
            swap1 = current.next        # First node of the pair
            swap2 = current.next.next   # Second node of the pair
        
            # Perform the swap
            swap1.next = swap2.next
            swap2.next = swap1
            current.next = swap2
        
            # Move the pointer two nodes ahead for the next swap
            current = swap1
        myList.head = dummy.next
        myList.traversal()
        
    
    def rotateListByNElements(self, myList, rotateBy):
        if not myList.head or rotateBy == 0:
            myList.traversal()
            return
        
        length = 1
        tail = myList.head
        while tail.next:
            length += 1
            tail = tail.next

        k = rotateBy % length
        if k == 0:
            myList.traversal()
            return
        
        splitting = length - k
        current = myList.head
        for _ in range(splitting - 1):
            current = current.next

        new_head = current.next 
        current.next = None 
        tail.next = myList.head 
        myList.head = new_head 
        myList.traversal()

    
    def removeDublicateElement(self,myList):
        head = myList.head
        current = head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        myList.traversal()
        
    
    def sortLinkedList(self,myList):
        temp = []
        head = myList.head
        current = head
        while current:
            temp.append(current.data)
            current = current.next
        temp.sort()
        
        node = CreateNode(-1)
        dummy = node
        for item in range(len(temp)):
            newNode = CreateNode(temp[item])
            dummy.next = newNode
            dummy = dummy.next
        myList.head = node.next
        myList.traversal()
    
    
    def deleteMiddleNodeOfLinkedList(self,myList):
        head = myList.head
        dummy = CreateNode(-1)
        dummy.next = head
        fastPtr = dummy
        slowPtr = dummy
        while  fastPtr.next.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        slowPtr.next = slowPtr.next.next
        myList.traversal()
        
    
    
    def oddEvenLinkedList(self,myList):
        head = myList.head
        
        oddDummy = CreateNode(-1)
        oddIndex = oddDummy
        evenDummy = CreateNode(-1)
        evenIndex = evenDummy
        index = 0
        
        while head is not None:
            if index % 2 == 0:
                evenIndex.next = CreateNode(head.data)
                evenIndex = evenIndex.next
            else:
                oddIndex.next = CreateNode(head.data)
                oddIndex = oddIndex.next
            index = index + 1
            head = head.next
        evenIndex.next = oddDummy.next
        myList.head = evenDummy.next
        myList.traversal()
        
        
    def detectCycleInLinkedList(self,myList):
        head = myList.head
        fastPtr = head
        slowPtr = head
        while fastPtr.next.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                print("Cycle Present")
                return
            else:
                print("No Cycle Found")
                return
        
        
    def isLinkedListPalindrome(self,myList):
        head = myList.head
        temp = []
        while head is not None:
            temp.append(head.data)
            head = head.next
        temp2 = temp[::-1]
        print(temp==temp2)
        
        
    def IntersectionOfTwoLinkedList(self,list1,list2):
        head1 = list1.head
        head2 = list2.head
        visited = {}
        while head1 is not None:
            visited[head1] = True
            head1 = head1.next
        while head2 is not None:
            if head2 in visited:
                print("Found")
                return
            head2 = head2.next
        print("Not Found")
        return
    
    
    def reverse2(self,myList,left=2,right=4):
        head = myList.head
        dummy = CreateNode(-1)
        dummy.next = head  # X -> 1 -> 2 -> 3 -> 4 -> 5
        
        prevNode = dummy
        currentNode = head
        
        # 1. Iterate till left-1
        for _ in range(left-1):
            prevNode = prevNode.next
            currentNode = currentNode.next
        
        # 2. Reverse between left and right i.e right-left+1 => 4-2+1 => 3 i.e 2,3,4 --> 4,3,2
        subListHead = currentNode
        previous = None
        for _ in range(right-left+1):
            tempNode = currentNode.next
            currentNode.next = previous
            previous = currentNode
            currentNode = tempNode
        
        # 3. Rejoin the parts
        prevNode.next = previous
        subListHead.next = currentNode
        
        # 4. Update the heads of a linked list
        myList.head = dummy.next
        myList.traversal()
        
        
    
        
ll1 = LinkedList()
ll1.insertEnd(1)
ll1.insertEnd(2)
ll1.insertEnd(3)
ll1.insertEnd(4)
ll1.insertEnd(5)


ll2 = LinkedList()
ll2.insertEnd(5)
ll2.insertEnd(6)
ll2.insertEnd(1)
ll2.insertEnd(8)
ll2.insertEnd(4)
ll2.insertEnd(5)

ll1.reverse2(ll1)