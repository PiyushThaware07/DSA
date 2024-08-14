'''
Fibonacci Number ~>  The fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. 

we already know starting 2 numbers i.e 0 and 1

0    1    1    2    3    5    8     13    21
         0+1  1+1  1+2  2+3  3+5   5+8   8+13
'''
from pickletools import optimize


class Solution:
    def brute(self,number):
        a = 0
        b = 1

        if number == 0:
            return a
        
        if number == 1:
            return b

        else:  
            print(a)
            print(b)
            for i in range(2,number+1):
                sum = a + b
                a = b
                b = sum
            return b


    def optimize(self,number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return self.optimize(number-1) + self.optimize(number-2)



s = Solution()
print("brute --> ",s.brute(3))
print("optimize --> ",s.optimize(3))