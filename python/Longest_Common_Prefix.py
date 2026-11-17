class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        i = 0
        if len(strs) == 1:
            return strs[0]
        while len(strs) >= 2 and len(strs[0]) > i  and len(strs[1]) > i:
            if strs[0][i] == strs[1][i]:
                prefix += strs[0][i]
                i += 1
            else:
                break
        i = 0
        j = 0
        while len(strs) > j :
            new_prefix = ""
            i = 0
            while len(strs[j]) > i and len(prefix) > i:
                if strs[j][i] == prefix[i]:
                    new_prefix += strs[j][i]
                    i += 1
                else:
                    break
            prefix = new_prefix
            j += 1
        if "" in strs:
            return ""
        return prefix
                    