class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

        return list(frequency.keys())[:k]