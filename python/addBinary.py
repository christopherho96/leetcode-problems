#https://leetcode.com/problems/add-binary/submissions/
class Solution(object):
    def addBinary(self, a, b):
        if a == "0" and b == "0":
            return a
        numA, numB, carry = int(a), int(b), 0
        stack = []
        while numA != 0 or numB != 0 or carry != 0:
            sum = (numA % 10 + numB % 10) + carry
            newDigit = sum % 2
            stack.append(newDigit)
            carry = sum // 2; numA /= 10; numB /= 10
        return "".join(map(str,stack[::-1]))              