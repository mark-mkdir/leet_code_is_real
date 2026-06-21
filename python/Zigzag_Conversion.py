class Solution(object):
    def convert(self, s, numRows):
        ANS = ""
        even = 0
        if numRows == 1:
            return s
        else:
            for i in range(numRows):
                j = i
                if i == numRows - 1:
                    ODD = False
                else:
                    ODD = True

                while j < len(s):
                    ANS = ANS + s[j]
                    if ODD or i == 0 :
                        j += (numRows - i-2) * 2 + 2
                        ODD = False
                    else:
                        j += even
                        if i != numRows-1:
                            ODD = True
                even += 2
            
            return ANS



