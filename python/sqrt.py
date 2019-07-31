#https://leetcode.com/problems/sqrtx/submissions/
#https://en.wikipedia.org/wiki/Newton%27s_method
class Solution(object):
    def mySqrt(self, x):
        r = x
        while r*r > x:
            r = (r + x//r)/2
        return r      