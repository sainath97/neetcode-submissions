class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 4 6
        # 1 1 2 8
        # 48 24 6 1

        # -1 0 1 2 3
        # 1 -1 0 0 0
        # 0  6 6 3 1
        # 0 -6 0 0 0
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        return [a * b for a, b in zip(prefix, suffix)]