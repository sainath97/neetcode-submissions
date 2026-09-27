class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:
        return self.bubblesort(nums)

     # Bubble Sort
    def bubblesort(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            swapped = False
            for j in range(len(nums) - i):
                if nums[j] > nums[j+1]:
                    swapped = True
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            # If no two elements were swapped in the inner loop, the array is sorted!
            if not swapped:
                break
        return nums