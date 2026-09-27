class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                k = i + 1
                temp1 = nums1[i]
                while k < m + 2:
                    temp2 = nums1[k]
                    nums1[k] = temp1
                    temp1 = temp2
                    k += 1
                nums1[i] = nums2[j]
                j += 1
                i += 1
            else:
                i += 1
        while j < n:
            nums1[i] = nums2[j]
            j += 1
            i += 1