class Solution:
    def reverseBits(self, n: int) -> int:
        binary = []
        while n:
            binary.append(n%2)
            n = n // 2
        rem = 32 - len(binary)
        binary.extend([0] * rem)
        reverse = 0
        for i in range(32):
            if binary[i]:
                reverse += 2 ** (32 - (i+1))
        return reverse