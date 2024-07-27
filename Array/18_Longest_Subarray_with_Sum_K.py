class Solution:
    def brute(self,arr,k):    # ~> O(n^3)
        '''
        step-1 ~> Generate all the sub-arrays whose sum of element is equal to k and store into the results.
        step-2 ~> iterate results and take the maximum length from a sub-array in results stored.
        '''
        results = []
        for i in range(0,len(arr)):
            submission = 0
            for j in range(i,len(arr)):
                submission = submission + arr[j]
                if submission == k:
                    results.append(arr[i:j+1])
        maximum = 0
        for k in range(0,len(results)):
            maximum = max(maximum,len(results[k]))
        print(maximum)

    
    def better(self,arr,k):   # ~> O(n^2)
        longest = 0
        for i in range(0,len(arr)):
            sumbmission = 0
            for j in range(i,len(arr)):
                sumbmission = sumbmission + arr[j]
                if sumbmission == k:
                    longest = max(longest,j-i+1)
        print(longest)

    


numbers = [1,2,3,1,1,1,1,2,3]
s = Solution()
s.brute(numbers,3)
s.better(numbers,3)