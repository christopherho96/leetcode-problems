#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution(object):
    #uses dictionray to keep track of passed characters
    def lengthOfLongestSubstringWithDict(self, s):
        chars = {}; i = 0; j=0; longest=0
        while j < len(s):
            if s[j] in chars:
                i=max(chars.get(s[j]) + 1, i)
            longest = max(longest, j-i+1)
            chars[s[j]] = j
            j+=1
        return longest

    #straight up sliding window
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2:
            return len(s)
        chars = {}
        i = 0; j=0; longest=0
        while j < len(s):
            if s[j] in chars:
                longest = max(longest, j-i)
                chars.pop(s[i])
                i+=1
            else:
                chars[s[j]] = j
                j+=1
        return max(longest, j-i)