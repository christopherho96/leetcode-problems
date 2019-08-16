#https://leetcode.com/problems/zigzag-conversion/submissions/
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        zizag = [""] * numRows; row = 0; stepper = 1
        for char in s:
            zizag[row] = zizag[row] + char
            row += stepper
            stepper = 1 if row == 0 else -1 if row == numRows-1 else stepper
        return ''.join(chars for chars in zizag)