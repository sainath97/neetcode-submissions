class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        def first_position(nums, target):
            l = 0
            r = len(nums) - 1
            while l < r:
                mid = l + ((r - l) // 2)
                if nums[mid] == target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            if nums[r] == target:
                return r
            return -1

        def last_position(nums, target):
            l = 0
            r = len(nums) - 1
            while l < r:
                mid = l + ((r - l + 1) // 2)
                if nums[mid] == target:
                    l = mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            if nums[r] == target:
                return r
            return -1

        return [first_position(nums, target), last_position(nums, target)]