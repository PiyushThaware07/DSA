class Solution:
    def FindLargest(self,arr):
        largest = 0
        for i in range(len(arr)):
            if arr[i] > largest:
                largest = arr[i]
        print(largest)
    
    def SecondLargest(self,arr):
        largest = arr[0]
        sLargest = -1
        for i in range(1,len(arr)):
            if arr[i] > largest:
                sLargest = largest
                largest = arr[i]
            if arr[i]<largest and arr[i]>sLargest:
                sLargest = arr[i]
        print(sLargest)

    def FindSmallest(self,arr):
        smallest = 100000
        for i in range(len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
        print(smallest)

    def SecondSmallest(self,arr):
        smallest1 = arr[0]
        smallest2 = 10000000
        for i in range(1,len(arr)):
            if arr[i] < smallest1:
                smallest2 = smallest1
                smallest1 = arr[i]
            if arr[i] > smallest1 and arr[i] < smallest2:
                smallest2 = arr[i]
        print(smallest2)

    def CheckSorted(self,arr):
        isSorted = False
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                isSorted = True
            else:
                isSorted = False
                break
        if(isSorted):
            print("Array is sorted")
        else:
            print("Array is not sorted")
    
    def RemoveDublicatedFromSorted(self,arr):
        ptr1 = 0
        ptr2 = 1
        for i in range(ptr2,len(arr)):
            if arr[i] != arr[ptr1]:
                arr[ptr1+1] = arr[i]
                ptr1 = ptr1 +1
        print(ptr1+1)

    def LeftRotateByOneElement(self,arr):
        temp = arr[0]
        for i in range(1,len(arr)):
            arr[i-1] = arr[i]
        arr[len(arr)-1] = temp
        print(arr)
    
    def LeftRotateByDPlaces(self,arr,d):
        d = d % len(arr)
        temp = arr[0:d]

        for i in range(d,len(arr)):
            arr[i-d] = arr[i]
        
        j = 0
        for i in range(len(arr)-d,len(arr)):
            arr[i] = temp[j]
            j = j+1
        print(arr)
    
    def ReverseArray(self,arr):
        up = 0
        down = len(arr)-1
        while up < down:
            temp = arr[up]
            arr[up] = arr[down]
            arr[down] = temp 
            up = up + 1
            down = down - 1
        print(arr)
    
    def MoveZerosAtEnd(self,arr):
        j = 0
        for i in range(0,len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j = j + 1
        
        for i in range(j,len(arr)):
            arr[i] = 0
        print(arr)

    def UnionOfTwoSortedArray(self):
        arr1 = [1,2,3,4,5]
        arr2 = [4,5,6,7,3,8]
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j<len(arr2):
            if arr1[i] <= arr2[j]:
                if arr1[i] not in result:
                    result.append(arr1[i])
                i = i + 1
            else:
                if  arr2[j] not in result:
                    result.append(arr2[j])
                j = j + 1
        for i in range(len(arr1)):
            if arr1[i] not in result:
                result.append(arr1[i])
        for j in range(len(arr2)):
            if arr2[j] not in result:
                result.append(arr2[j])
        print(result)

    
    def IntersectionOfTwoSortedArray(self):
        arr1 = [1,2,2,3,3,4,5,6]
        arr2 = [2,3,3,5,6,6,7]
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j<len(arr2):
            if arr1[i] < arr2[j]:
                i = i + 1
            elif arr1[i] > arr2[j]:
                j = j + 1
            else:
                result.append(arr1[i])
                i = i + 1
                j = j + 1
        print(result)

    def FindMissingNumber(self):
        arr = [1,2,3,5]
        n = 5
        sum_of_n_natual_numbers = int((n*(n+1))/2)
        sum_of_elements_of_arr = 0
        for i in range(len(arr)):
            sum_of_elements_of_arr = sum_of_elements_of_arr + arr[i]
        print(sum_of_n_natual_numbers-sum_of_elements_of_arr)

    
    def MaximumConsecutiveOnce(self):
        arr = [0,1,1,0,1,1,1,0,1,1]
        maximum = 0
        counter = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                counter = counter+1
                maximum = max(maximum,counter)
            else:
                counter = 0
        print(maximum)

    
    def FindNumberThatAppearsOnce(self):
        arr = [1,2,2,2,3,3,4,4,5,5,5,6,6]
        hashMap = {}
        for i in range(len(arr)):
            if arr[i] in hashMap:
                hashMap[arr[i]] = hashMap[arr[i]] + 1
            else:
                hashMap[arr[i]] = 1
        for j in hashMap:
            if hashMap[j] == 1:
                print(j)
                break
    
    def MoveAllNegativeNumberToRightButDontChangeOrder(self):
        arr = [-2,5,-5,0,3,-9]
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j] >= 0 and arr[j]>arr[i]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    break
        print(arr)
        











numbers = [11,12,13,14,15]        
s = Solution()
# s.FindLargest(numbers)
# s.SecondLargest(numbers)
# s.FindSmallest(numbers)
# s.SecondSmallest(numbers)
# s.CheckSorted(numbers)
# s.LeftRotateByDPlaces(numbers,2)
# s.RemoveDublicatedFromSorted(numbers)
# s.LeftRotateByOneElement(numbers)   
# s.ReverseArray(numbers)   
# s.MoveZerosAtEnd(numbers)
# s.UnionOfTwoSortedArray()
# s.IntersectionOfTwoSortedArray()
# s.FindMissingNumber()
# s.MaximumConsecutiveOnce()
# s.FindNumberThatAppearsOnce()
s.MoveAllNegativeNumberToRightButDontChangeOrder()