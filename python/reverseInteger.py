# https://leetcode.com/problems/reverse-integer/submissions/
class Solution(object):
    def reverse(self, x):
        xAbs = abs(x)
        answer = 0
        while xAbs != 0:
            answer = answer*10 + xAbs%10
            xAbs /= 10
        if answer > 2**31 -1 or answer < -2**31:
            return 0
        return answer if x > 0 else -answer