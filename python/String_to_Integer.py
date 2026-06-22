class Solution(object):
    def myAtoi(self, s):
        negative =  False
        find = False
        sum = 0
        for i in range(len(s)):
            if s[i] == '-' and not find:
                negative = True
                find = True
            elif s[i].isdigit():
                find = True
                sum *= 10
                sum += int(s[i])
            elif s[i] == " ":
                if not find:
                    pass
                else:
                    if negative :
                        if -sum < -2147483648 :
                            return -2147483648
                        else:
                            return -sum
                    else:
                        if sum > 2147483647:
                            return 2147483647
                        else:
                            return sum
            elif  s[i] == "+":
                if not find:
                    find = True
                else:
                    if negative :
                        if -sum < -2147483648 :
                            return -2147483648
                        else:
                            return -sum
                    else:
                        if sum > 2147483647:
                            return 2147483647
                        else:
                            return sum
            else:

                if negative :
                    if -sum < -2147483648 :
                        return -2147483648
                    else:
                        return -sum
                else:
                    if sum > 2147483647:
                        return 2147483647
                    else:
                        return sum
        
        if negative :
            if -sum < -2147483648 :
                return -2147483648
            else:
                return -sum
        else:
            if sum > 2147483647:
                return 2147483647
            else:
                return sum