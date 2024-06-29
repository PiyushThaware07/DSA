# Left rotate an array by d-places

class Solution:
    def better(self,arr,n,d):
        d = d % n           # suppose d=8  => 8/5 => 3 (Roatation)
        temp = arr[0:d]   # store element at the starting till d places
        for i in range(d,n):
            arr[i-d] = arr[i]
        
        j = 0
        for i in range(n-d,n):   # n-d => 7-3 => 4 index
            arr[i] = temp[j]
            j = j+1
        print(arr)

  





nums = [1,2,3,4,5,6,7]
s = Solution()
s.better(nums,len(nums),19)