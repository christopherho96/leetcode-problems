# https://leetcode.com/problems/generate-parentheses/submissions/
# n = 3
# output = ["((()))","(()())","(())()","()(())","()()()"]

class Solution(object):
    def generateParenthesis(self, n):
        answer = []
        self.validateBrackets(answer, "", 0, 0, n)
        return answer
    
    #keep track of the amount of left and right brackets used
    # use recursion to iterate through all the different combinations of
    # n open-close brackets
    def validateBrackets(self, answer, brackets, left, right, n):
        if len(brackets) == 2*n:
            answer.append(brackets)
        else:
            # We know that if the required brackets is n, then left number of open brackets '('
            # must be n. So until answer has n '(' brackets, we keep adding them
            if left<n :
                self.validateBrackets(answer, brackets+"(", left+1, right, n)
            # For every left bracket, there must be a closing right bracket ')'.
            # So until we have the same amount of closing brackets as opening brackets,
            # we continue to add closing brackets
            if right<left:
                self.validateBrackets(answer, brackets+")", left, right+1, n)