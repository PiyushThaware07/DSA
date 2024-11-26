'''
Left rotate an array by one place :
Example : [1,2,3,4,5]
        : [2,3,4,5,1]

Explanation:
    1. In a left rotation, the first element of the array is moved to the end, and the rest of the elements are shifted one position to the left.
    2. For the input [1, 2, 3, 4, 5]:
    - The first element `1` is temporarily stored.
    - All elements from index `1` to the last are shifted one position to the left.
    - The stored first element `1` is then placed at the last index.
    3. Result: [2, 3, 4, 5, 1]
'''

class Solution:
    def leftRotate(self,arr,n):
        temp = arr[0]
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[n-1] = temp
        print(arr)

nums = [1,2,3,4,5]
[2,3,4,5]
s = Solution()
s.leftRotate(nums,len(nums))
