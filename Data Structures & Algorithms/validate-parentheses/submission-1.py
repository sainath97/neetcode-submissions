class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                last_ch = stack.pop()
                if last_ch != mapper[ch]:
                    return False
        return not stack