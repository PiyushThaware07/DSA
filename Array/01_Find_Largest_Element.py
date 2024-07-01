'''
Find the largest element in an array
1. Brute Force
2. Better
3. Optimized
'''

# & 1. Brute Force
class Solution:
    # Brute force : sort an array and simply print last element of an array
    def brute(self,arr):
        # Using Insertion Sort
        n = len(arr)
        for i in range(1,n):
            temp = arr[i]
            prev = i-1
            while(prev>=0 and arr[prev]>temp ):
                arr[prev+1] = arr[prev]
                prev = prev-1
            arr[prev+1]= temp
        print(arr[n-1])

    def optimized(self,arr):
        n = len(arr)
        largest = arr[0]
        for i in range(n):
            if arr[i] > largest:
                largest = arr[i]
        print(largest)

nums = [23,1,45,32,57,4,0]
s = Solution()
s.brute(nums)
s.optimized(nums)




