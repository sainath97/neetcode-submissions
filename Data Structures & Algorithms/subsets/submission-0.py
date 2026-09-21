class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]

        for num in nums:
            n = len(subs)
            for i in range(n):
                new_subset = subs[i].copy()
                new_subset.append(num)
                subs.append(new_subset)

        return subs

        # subs=[[]]
		
		# num = 1
		# 	n = 1
		# 		i=0
		# 			subs = [[], [1]]
		
		# num = 2
		# 	n = 2
		# 		i=0
		# 			subs = [[], [1], [2]]
		# 		i=1
		# 			subs = [[], [1], [2], [1,2]]
		
		# num = 3
		# 	n = 4
		# 		i=0
		# 			subs = [[], [1], [2], [1,2], [3]]
		# 		i=1
		# 			subs = [[], [1], [2], [1,2], [3], [1,3]]
		# 		i=2
		# 			subs = [[], [1], [2], [1,2], [3], [1,3], [2,3]]
		# 		i=3
		# 			subs = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
		