class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest_sequence_length = 0

        for num in unique_nums:
            if num - 1 not in unique_nums:
                current_num = num
                current_sequence_length = 1
                while current_num + 1 in unique_nums:
                    current_sequence_length += 1
                    current_num += 1
                longest_sequence_length = max(longest_sequence_length, current_sequence_length)

        return longest_sequence_length