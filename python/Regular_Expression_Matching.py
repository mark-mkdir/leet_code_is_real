class Solution(object):
    def isMatch(self, s, p):
        i = 0
        j = 0
        Is_match = True
        while i != len(s) and j != len(p):
            a = s[i]
            b = p[j]
            if p[j] == s[i] or p[j] == '.':
                i += 1
                j += 1
            elif p[j] == '*':
                while i < len(s) and s[i] == s[i-1]:
                    i = i + 1
                j = j + 1 
            else:
                Is_match = False
                break
        if i == len(s) and j == len(p):
            Is_match = True
        elif len(s) >= 2 and p == ".*":
            Is_match = True
        else:
            Is_match = False
        return Is_match

s = "aa"
p = "a*"
solution = Solution()
print(solution.isMatch(s, p))
