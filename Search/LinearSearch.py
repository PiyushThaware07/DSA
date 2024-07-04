class Solution:
    def search(self,arr,find):
        for i in range(0,len(arr)):
            if arr[i]==find:
                print("Found at index --> ",i)
                break

nums = [100,1,2,4,33,23,54]
s = Solution()
find = 4
s.search(nums,find)