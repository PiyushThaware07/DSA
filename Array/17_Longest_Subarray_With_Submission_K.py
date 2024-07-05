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
        longest = 0
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                submission = 0
                for m in range(i, j):
                    submission = submission + arr[m]
                    # print(arr[m], end=" ")
                if submission == k:
                    longest = max(longest, j - i + 1)
        print(longest)
                    
                


        
nums = [2,3,5,1,9]
k = 10
s = Solution()
s.brute(nums,k)

nums = [2,3,5,1,9]
for j in range(len(nums)-1,-1,-1):
    print(nums[j])