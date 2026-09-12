class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s==t:
            return True
        if len(s)!=len(t):
            return False
        frequency = {}
        for ch in s:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1
        for ch in t:
            if ch in frequency:
                frequency[ch] -= 1
            else:
                return False
            if frequency[ch] == 0:
                del frequency[ch]
        return not frequency