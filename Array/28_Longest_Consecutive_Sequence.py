'''
Longest Consecutive Sequence --> Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.
    Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

    Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
'''
class Solution:
    def brute(self,arr):
        n = len(arr)
        longest = 1
        for i in range(0,n):
            temp = arr[i]
            count = 0
            for j in range(0,n):
                if arr[j] == temp:
                    print("Before --> ","count = ",count,"temp =",temp)
                    temp = temp + 1
                    count = count + 1
                    print("\tAfter --> ","count = ",count,"temp =",temp)
                    b


        
numbers = [100,4,200,1,3,2]
s = Solution()
s.brute(numbers)