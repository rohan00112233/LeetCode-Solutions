class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq ={}
        for name in s:
            if name not in freq:
                freq[name] = 1
            else:
                freq[name] += 1
        
        for name in range(len(s)):
            if freq[s[name]] ==  1:
                return name
        return -1 