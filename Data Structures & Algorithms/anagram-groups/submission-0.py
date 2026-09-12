class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        res = []
        for str in strs:
            frequency = {}
            for ch in str:
                if ch in frequency:
                    frequency[ch] += 1
                else:
                    frequency[ch] = 1
            map_key = frozenset(frequency.items())
            if map_key in anagram_map:
                anagram_map[map_key].append(str)
            else:
                anagram_map[map_key]=[str]
        return list(anagram_map.values())