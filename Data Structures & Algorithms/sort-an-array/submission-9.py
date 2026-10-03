class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    # Merge Sort
    def merge_sort(self, nums, left, right):
        #print(nums[left: right + 1])
        if left >= right:
            return
        mid = left + ((right - left) // 2)
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        a1 = nums[left : mid + 1]
        a2 = nums[mid + 1: right + 1]
        #print((a1, a2))
        i, j, k = 0, 0, left
        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                nums[k] = a1[i]
                i += 1
            else:
                nums[k] = a2[j]
                j += 1
            k += 1
        while i < len(a1):
            nums[k] = a1[i]
            i += 1
            k += 1
        while j < len(a2):
            nums[k] = a2[j]
            j += 1
            k += 1
        #print(nums)

    # Counting Sort
    def counting_sort(self, nums: list[int]) -> list[int]:
        start = min(nums)
        end = max(nums)
        frequency = [0] * (end - start + 1)
        for num in nums:
            frequency[num - start] += 1
        for i in range(1, len(frequency)):
            frequency[i] += frequency[i - 1]

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[frequency[nums[i] - start] - 1] = nums[i]
            frequency[nums[i] - start] -= 1
        return res

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