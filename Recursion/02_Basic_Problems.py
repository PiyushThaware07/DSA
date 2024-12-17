# PROBLEM 01 : Print name 5 times.
from ctypes import pointer


def function01(name,count):
    if count > 5:
        return
    print(name)
    function01(name,count+1)
function01("james smith",1)
    
    
# PROBLEM 02 : Print Linearly from 1 to N
def function02(count):
    if count < 100:
        print(count,end=" ")
    else:
        return
    function02(count+1)
function02(1)
    
# PROBLEM 03 : Print Linearly from N to 1
def function03(count):
    if count > 0:
        print(count,end=" ")
    else:
        return
    function03(count-1)
function03(100)

# PROBLEM 04 : Submission of N numbers. (Parameterised Recursion)
def function04(num,submission):
    if num < 1:
        print("\n",submission)
        return
    function04(num-1,submission+num)
function04(10,0)

'''
|   func(1 ,54+1 = 55)   | <-- Base Condition Meets Here
|   func(2 ,52+2 = 54)   |
|   func(3 ,49+3 = 52)   |
|   func(4 ,45+4 = 49)   |
|   func(5 ,40+5 = 45)   |
|   func(6 ,34+6 = 40)   |
|   func(7 ,27+7 = 34)   |
|   func(8 ,19+8 = 27)   |
|   func(9 ,10+9 = 19)   |
|   func(10,0+10 = 10)   | <--- Function Call Starts Here
|------------------------|
|         STACK          |
|------------------------|
'''


# PROBLEM 05 : Submission of N numbers. (Functional Recursion)
def function05(num):
    if num == 0:
        return num
    return num + function05(num-1)
print(function05(3))
'''
|   1 + function(1-1=0)    |
|   2 + function(2-1=1)    |
|   3 + function(3-1=2)    |
|--------------------------|
'''


# PROBLEM 6 : Factorial Of N numbers
def function06(num):
    if num == 0 or num == 1:
        return 1
    return num * function06(num-1)
print(function06(5))



# PROBLEM 7 : Reverse an array
def function07(nums,left,right):
    if left >= right:
        return nums
    nums[left],nums[right] = nums[right],nums[left]
    function07(nums,left+1,right-1)
    return nums
nums = [1,2,3,4,5]
print(function07(nums,0,len(nums)-1))



# PROBLEM 08 : Check is string palindrome
def function08(string,left,right):
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return function08(string,left+1,right-1)
string = "MADAM"
print(function08(string,0,len(string)-1))
    
# PROBLEM 09 : fibonacci series --> Multiple Recursion Calls
def function09(num):
    if num <= 1:
        return num
    last = function09(num-1) 
    secondLast = function09(num-2)
    return last + secondLast
print(function09(8))
'''
    function09(8)
      /       \
 function09(7)   function09(6)
    /      \       /      \
function09(6)  function09(5) function09(5) function09(4)
   /   \       /   \       /   \       /   \
function09(5) function09(4) function09(4) function09(3)
   /   \    /   \    /   \    /   \    /   \
function09(4) function09(3) function09(3) function09(2)
   /   \    /   \    /   \    /   \
function09(3) function09(2) function09(2) function09(1)
   /   \    /   \    /   \    /   \
function09(2) function09(1) function09(1) function09(0)

'''


# PROBLEM 10 : Return sum of all odd number till N
def function10(index,submission,nums):
    if index > nums:
        return submission
    if index % 2 != 0:
        submission += index
    return function10(index+1,submission,nums)
print(function10(1,0,9))


# PROBLEM 11 : Recursion on Subsequences -> Printing Subsequences
def function11(index,nums,result):
    if index >= len(nums):
        result.append()


nums = [1,5,7]
result = []
function11(0,nums,result)

        
