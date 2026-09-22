class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                print(i)
                count += 1
        return count

    def isPrime(self, n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True