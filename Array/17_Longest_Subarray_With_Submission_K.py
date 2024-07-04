'''
Find the longest sub-array with submission k 

nums = [1,2,3,1,1,1,4,2,3]
k = 3

so , here [1,2,3] is also an sub-array
[1,1,1] , [1,1,4] ...
'''

class Solution:
    def brute(self,arr,k):
        # step-1 --> generate all the sub-array
        # step-2 --> check the len of each sub-array if it is equal to k means we got the longest sub-array.
        sub_arrays = []
        for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                # print(sub_arrays)
                sub_arrays.append(arr[i:j+1])
        for m in range(0,len(sub_arrays)):
            if len(sub_arrays[m]) == k:
                print(sub_arrays[m])
                return
                


        
nums = [1,2,3,1,1,1,4,2,3]
k = 3
s = Solution()
s.brute(nums,k)