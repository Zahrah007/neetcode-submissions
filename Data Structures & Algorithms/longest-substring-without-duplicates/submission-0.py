class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0 
        L = 0
        charSet = {}

        for R in range(len(s)):
            if s[R] in charSet: 
                L = max(charSet[s[R]] + 1, L)
            charSet[s[R]] = R
            length = max(length, R - L + 1)
        return length 
