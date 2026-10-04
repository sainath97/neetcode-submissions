class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsWithIndex = []
        for i in range(len(nums)):
            numsWithIndex.append([nums[i], i])
        numsWithIndex.sort(key=lambda x: x[0])
        i, j = 0, len(nums) - 1
        while i < j:
            curr_sum = numsWithIndex[i][0] + numsWithIndex[j][0]
            if curr_sum == target:
                return [numsWithIndex[i][1], numsWithIndex[j][1]]
            elif curr_sum < target:
                i += 1
            else:
                j -= 1
        return []