class Solution:
    def brute(self,arr):
        n = len(arr)
        result = []
        for i in range(0,n):
            leader = arr[i]
            for j in range(i+1,n):
                if arr[j] > leader:
                    break
                else:
                    result.append(leader)
                    break
        result.append(arr[n-1])
        print(result)
    
    def optimal(self,arr):
        n = len(arr)
        maximum = 0
        result = []
        for i in range(n-1,-1,-1):
            if arr[i] >= maximum:
                result.append(arr[i])
            maximum = max(arr[i],maximum)
        result.reverse()
        print(result)



                


numbers = [16,17,4,3,5,2]
numbers = [10,4,2,4,1]
s = Solution()
# s.brute(numbers)
s.optimal(numbers)