class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2) + 1
        half = total // 2

        if (len(B) < len(A)):
            A, B = B, A
        
        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2
            j = half - i 
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return max(Aleft, Bleft)
            elif Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
                l = i + 1