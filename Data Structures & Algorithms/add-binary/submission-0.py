class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            sum = carry + int(a[i]) + int(b[j])
            res = str(sum % 2) + res
            carry = sum // 2
            i -= 1
            j -= 1
        while i >= 0:
            sum = carry + int(a[i])
            res = str(sum % 2) + res
            carry = sum // 2
            i -= 1
        while j >= 0:
            sum = carry + int(b[j])
            res = str(sum % 2) + res
            carry = sum // 2
            j -= 1
        if carry == 1:
            res = str(carry) + res
        return res