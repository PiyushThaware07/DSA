class Solution:
    def brute(self,string):
        n = string
        hashMap = {}
        for char in string:
            if char not in hashMap:
                hashMap[char] = 1
        print(hashMap)
        print(hashMap.__len__())

string = "pwwkew"
s = Solution()
s.brute(string)

