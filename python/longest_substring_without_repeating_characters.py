class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0 
        temp = 0
        word = ""
        if len(s) != 0:
            for i in range(len(s)):
                word = ""
                temp = 0
                for j in range(i, len(s)):
                    if s[j] not in word:
                        word = word + s[j]
                        temp += 1
                        longest = max(temp, longest)
                    else:
                        temp = 1
                        break
            return longest
        else:
            return 0