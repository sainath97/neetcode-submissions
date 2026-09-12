class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = [0, 0, 0]
        # for num in nums:
        #     count[num] += 1
        # k=0
        # for i in range(3):
        #     for j in range(count[i]):
        #         nums[k] = i
        #         k += 1

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        l, i, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
            else:
                i+=1
