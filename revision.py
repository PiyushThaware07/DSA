target = [1,2,3,4]
nums = [2,3,1,4]
target.sort()
nums.sort()
if len(target) != len(nums):
    print("No")

for i in range(len(target)):
    if nums[i] != target[i]:
        print("YES")
