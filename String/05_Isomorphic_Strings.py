'''
Isomorphic Strings


Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true
    Explanation : 
        s = "e g g"
        t = "a d d"
        1. replace e by d in s
        s = "a g g"
        2. replace g by d in s
        s = "a d g"
        3. replace g by d in s 
        s = "a d d"

Example 2 : 
    Input: s = "foo", t = "bar"
    Output: false
    Explanation : 
        s = "f o o"
        t = "b a r"
        1. replace f by b in s
        s = "b o o" 
        2. replace o by a in s 
        s = "b a o"
        3. replace o by r in s by since in step-2 "o->a" so modification not allowed
        s = "b a o"
        therefore it is not isomorphic
'''


class Solution:
    def optimized(self,string1,string2):
        # check string have equal length's
        if len(string1) != len(string2):
            print("not isomorphic")
        
        hashMapST = {}
        hashMapTS = {}
        for i in range(0,len(string1)):
            c1 = string1[i]
            c2 = string2[i]
            if (c1 in hashMapST and hashMapST[c1] != c2) or (c2 in hashMapTS and hashMapTS[c2] != c1):
                print(False)
            hashMapST[c1] = c2
            hashMapTS[c2] = c1
        print(True)




            hashMapST[c1] = c2
            hashMapTS[c2] = c1

        
                






            






s = "eggp"
t = "addd"
sol = Solution()
sol.optimized(s,t)
