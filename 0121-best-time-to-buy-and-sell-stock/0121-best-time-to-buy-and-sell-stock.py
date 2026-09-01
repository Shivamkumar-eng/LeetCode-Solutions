class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min1=float('inf')
        max1=0
        for price in prices:
            if price<min1:
                min1=price
            elif price-min1>max1:
                max1=price-min1
        return max1
