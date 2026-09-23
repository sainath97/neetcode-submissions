class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        missing = []
        for i in range(len(nums)):
            if i + 1 not in nums_set:
                missing.append(i + 1)
        return missing

        #return [i + 1 for i in range(len(nums)) if i + 1 not in nums_set]