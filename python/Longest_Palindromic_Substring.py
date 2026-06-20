class Solution(object):
    def longestPalindrome(self, s):
        CW = ""
        LPD = ""
        for i in range(len(s)):
            CW = ""
            j = i+1
            CW += s[i]
            if LPD == "":
                LPD = CW
            while j < len(s) and len(CW) < len(s):
                CW += s[j]
                if len(CW) > len(LPD):
                    if CW == CW[::-1]:
                        LPD = CW
                j += 1
        return LPD

