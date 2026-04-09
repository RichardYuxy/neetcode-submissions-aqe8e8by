class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestP = prices[0]
        res=0

        for price in prices:
            if price-lowestP > res:
                res=price-lowestP
            if lowestP > price:
                lowestP = price

        return res
