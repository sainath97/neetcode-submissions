class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        merged_string = ""
        i, j = 0, 0
        while i < l1 and j < l2:
            merged_string += word1[i] + word2[j]
            i += 1
            j += 1
        if i < l1:
            merged_string += word1[i:]
        if j < l2:
            merged_string += word2[j:]
        return merged_string