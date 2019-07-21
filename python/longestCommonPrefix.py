#https://leetcode.com/problems/longest-common-prefix/submissions/
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        commonPrefix = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            currentString = strs[i]
            for index in range(0, min(len(commonPrefix), len(currentString))):
                if commonPrefix[index] == currentString[index]:
                    temp += commonPrefix[index]
                else:
                    break
            commonPrefix = temp
        return commonPrefix

    def longestCommonPrefixRecursion(self, strs):
        return prefixRecursion(strs, 0, len(strs) -1)
        
    def prefixRecursion(strs, start, end):
        commonPrefix = ""
        if(start==end): 
            return strs[start]

        middle = start + (end - start) / 2
        left = prefixRecursion(strs, start, middle)
        right = prefixRecursion(strs, middle + 1, end)

        for index in range(0, min(len(left), len(right))):
            if left[index] == right[index]:
                commonPrefix += + left[index]
            else:
                return commonPrefix