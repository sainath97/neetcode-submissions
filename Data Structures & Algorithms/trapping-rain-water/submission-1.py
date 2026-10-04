class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        current_left_max = left_max[0]
        for i in range(1, n):
            left_max[i] = current_left_max
            current_left_max = max(current_left_max, height[i])
        
        right_max[-1] = height[-1]
        current_right_max = right_max[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = current_right_max
            current_right_max = max(current_right_max, height[i])
        
        amount = 0
        for i in range(1, n-1):
            curr_amount = min(left_max[i], right_max[i]) - height[i]
            if curr_amount > 0:
                amount += curr_amount
        return amount