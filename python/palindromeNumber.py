#https://leetcode.com/problems/palindrome-number/submissions/
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        answer = 0
        tempX = x
        while( tempX != 0):
            answer = (answer * 10) + (tempX % 10)
            tempX /= 10
            
        return x == answer