class Solution:
    def brute(self,arr):
        for p1 in range(0,len(arr)):
            for p2 in range(p1+1,len(arr)):
                if arr[p1] >  arr[p2]:
                    temp = arr[p1]
                    arr[p1] = arr[p2]
                    arr[p2] = temp
        print(arr)

    def optimal(self,arr):
        zeros = 0
        onces = 0
        twos = len(arr)-1
        while (onces<=twos):
            if arr[onces] == 0:
                temp = arr[zeros]
                arr[zeros] = arr[onces]
                arr[onces] = temp 
                zeros = zeros + 1
                onces = onces + 1
            elif arr[onces] == 2:
                temp = arr[onces]
                arr[onces] = arr[twos]
                arr[twos] = temp
                twos = twos - 1
            else:
                onces = onces + 1
        print(arr)

nums = [2,0,2,1,1,0]
s = Solution()
s.brute(nums)
s.optimal(nums)
