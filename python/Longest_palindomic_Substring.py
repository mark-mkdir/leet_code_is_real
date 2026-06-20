class Solution(object):
    def longestPalindrome(self, s):
        
        longest = ""

        for i in range(len(s)) :
            for j in range(i+1,len(s)):
                if