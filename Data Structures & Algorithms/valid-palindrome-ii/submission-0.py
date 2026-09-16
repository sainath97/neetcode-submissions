class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        skipped = False
        while (l < r):
            if (s[l] == s[r]):
                l += 1
                r -= 1
            elif not skipped and (r - l) > 1:
                if (s[l+1] == s[r]):
                    l += 1
                    skipped = True
                elif (s[l] == s[r-1]):
                    r -= 1
                    skipped = True
                else:
                    return False
            else:
                return False
        return True