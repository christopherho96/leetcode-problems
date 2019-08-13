#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution(object):
    def lengthOfLongestSubstringWithDict(self, s):
        chars = {}; i = 0; j=0; longest=0
        while j < len(s):
            if s[j] in chars:
                i=max(chars.get(s[j]) + 1, i)
            longest = max(longest, j-i+1)
            chars[s[j]] = j
            j+=1
        return longest
    def lengthOfLongestSubstring(self, s):
    