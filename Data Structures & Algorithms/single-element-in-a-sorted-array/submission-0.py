class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if mid == 0:
                if nums[mid] != nums[mid + 1]:
                    return nums[mid]
                else:
                    left = mid + 2
                    break
            elif mid == len(nums) - 1:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
                else:
                    right = mid - 2
                    break
            if (nums[mid] != nums[mid - 1]) and (nums[mid] != nums[mid + 1]):
                return nums[mid]
            elif mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1