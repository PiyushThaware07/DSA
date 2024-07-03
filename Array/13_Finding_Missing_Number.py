''' 
find the missing number i an array for a value
nums = [1,2,4,5] 
N = 5
so here while comparing N to nums we notice that 3 is missing.
'''

class Solution:
    def sample(self,arr,N):
        i = 1
        while i<=N:
            if i not in arr:
                print(i)
                break
            i = i+1
    
    def brute(self,arr,N):
        for i in range(1,N+1):
            flag = 0
            for j in range(0,len(arr)):
                if arr[j] == i:
                    flag = 1
                    break
            if(flag == 0):
                print(i)
                return
            


nums = [1,2,4,5]
N = 5
s = Solution()
s.sample(nums,N)
s.brute(nums,N)

