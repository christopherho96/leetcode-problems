class Solution(object):
    def insertFive(self, N):
        i=0; right=0
        if N<0:
            return int('5' + str(N/-1)) * -1
        while N != 0:
            digit = N%10
            N /= 10
            right = digit*pow(10,i) + right
            if 5 >= digit:
                return N*pow(10,i+2) + 5*pow(10,i+1) + right
            i += 1
        return 5*pow(10,i) + right