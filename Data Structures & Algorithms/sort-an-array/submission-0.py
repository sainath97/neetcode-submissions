class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        else:
            pivot = self.median([nums[0], nums[-1], nums[len(nums)//2]])
            return (
                self.sortArray([num for num in nums if num < pivot]) +
                [num for num in nums if num == pivot] +
                self.sortArray([num for num in nums if num > pivot])
            )

    def median(self, nums: List[int]) -> int:
        nums.sort()
        return nums[1]
