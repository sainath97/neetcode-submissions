class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 1
        while n:
            if n & 1:
                res += 2 ** (32 - count)
            n = n >> 1
            count += 1
        return res