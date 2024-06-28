'''
Left rotate an array by one place :
Example : [1,2,3,4,5]
        : [2,3,4,5,1]  
Explanation : As you can see 2 at index 0
                             3 at index 1
                             4 at index 2 
                             5 at index 3
                             1 at index 4
Solution : Store the first element into the temp
           temp = arr[0] = 1
           start loop from index=1 to n
           store 2 into arr[index-1]  i.e index-1 = 1-1 = 0 : arr[0] = 2
           repeat similar for 3,4,5 till the end of the list
           at the end insert temp to the last index
'''

class Solution:
    def leftRotate(self,arr,n):
        temp = arr[0]
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[n-1] = temp
        print(arr)

nums = [1,2,3,4,5]
[2,3,4,5]
s = Solution()
s.leftRotate(nums,len(nums))
