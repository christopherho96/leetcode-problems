#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {')': '(', '}':'{', ']':'['}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif dict.get(char) != stack.pop():
                return False
        return len(stack) == 0        