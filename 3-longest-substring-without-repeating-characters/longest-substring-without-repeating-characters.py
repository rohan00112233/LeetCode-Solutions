class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            visited =set()
            for j in range(i,len(s)):
                if s[j] in visited:
                    break
                else:
                    visited.add(s[j])
                    maxlen = max(maxlen,j-i+1)
        return maxlen        