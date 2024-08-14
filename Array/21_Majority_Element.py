'''
Majority Element

Given an array nums of size n, return the majority element.
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def brute(self,arr):
        for i in range(len(arr)):
            count = 0
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count = count + 1
            if count > int(len(arr)/2):
                print(arr[i])
                return


    def better(self,arr):
        hashMap = {}
        for i in range(len(arr)):
            if arr[i] in hashMap:
                hashMap[arr[i]] = hashMap[arr[i]] + 1
            else:
                hashMap[arr[i]] = 1
        for key in hashMap:
            if hashMap[key] > int(len(arr)/2):
                print(key)
                return

    def optimal(self,arr): # ! Moore's Voting Algorithm
        count = 0
        element = None 
        for i in range(len(arr)):
            if count == 0:
                count = count + 1
                element = arr[i]
            elif arr[i] == element:
                count = count + 1
            else:
                count = count - 1
        print(element)

nums = [2,2,1,1,1,2,2]
s = Solution()
s.brute(nums)
s.better(nums)
s.optimal(nums)