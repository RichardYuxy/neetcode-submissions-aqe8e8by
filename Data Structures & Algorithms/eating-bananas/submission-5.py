class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            current = (l + r) // 2
            time = 0

            for pile in piles:
                time += (pile + current - 1) // current
            if time <= h:
                res = current
                r = current - 1

            else:
                l = current +1
        return res