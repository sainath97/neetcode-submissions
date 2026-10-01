class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        unique_count = i + 1
        
        # Below is not required as it doesn't matter what nums contains after unique_count element
        # nums[:] = nums[:unique_count]
        
        return unique_count