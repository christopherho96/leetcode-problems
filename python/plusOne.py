# https://leetcode.com/problems/plus-one/submissions/ 

class Solution(object):
    def plusOneStringConversion(self, digits):
        number = int("".join(map(str, digits))) + 1
        return [int(d) for d in str(number)]
    
    def plusOneIterative(self, digits):
        carry = 1
        index = len(digits)-1
        while index >= 0:
            newDigit = digits[index] + carry
            digits[index] = newDigit % 10
            carry = newDigit // 10
            index -= 1
                
        if carry == 1:
            digits.insert(0, 1)
        
        return digits

print(Solution().plusOneStringConversion([1,8,9]))
print(Solution().plusOneIterative([1,8,9]))