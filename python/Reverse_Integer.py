class Solution(object):
    def reverse(self, x):

        sum =  0
        if x < 0 :
            negative = True
            x = x * -1
        else:
            negative = False

        while x > 0 :
            print(sum,x)
            sum *= 10
            if sum == 0 and x % 10 == 0 :
                pass
            else:
                sum += x % 10
            x = x // 10

        if sum > 2147483647 or sum < -2147483648 :
            return 0
        if negative :
            return -sum
        else:
            return sum

        