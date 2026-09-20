class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        result = []
        current = []
        self.arrange(nums, current, result, visited)
        return result

    def arrange(self, nums, current, result, visited):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if visited[i] == False:
                visited[i] = True
                current.append(nums[i])
                self.arrange(nums, current, result, visited)
                visited[i] = False
                del current[-1]