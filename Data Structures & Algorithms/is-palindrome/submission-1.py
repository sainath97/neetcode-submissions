class Solution:
    def isPalindrome(self, s: str) -> bool:
        #cleaned_input = "".join([ch for ch in s if ch.isalnum()]).lower()
        #l, r = 0, len(cleaned_input) - 1
        l, r = 0, len(s) - 1
        while(l < r):
            # if cleaned_input[l] == cleaned_input[r]:
            #     l += 1
            #     r -= 1
            # else:
            #     return False
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower():
                l, r = l + 1, r - 1
            else:
                return False
        return True