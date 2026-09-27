class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:
        return self.insertion_sort(nums)

    # Insertion Sort
    def insertion_sort(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

    # Selection Sort
    def selection_sort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            if min_index != i:
                nums[min_index], nums[i] = nums[i], nums[min_index]
        return nums

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