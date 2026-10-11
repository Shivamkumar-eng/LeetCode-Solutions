
class Solution:
    def calculateHours(self, piles, speed):
        hours = 0

        for pile in piles:
            hours += (pile + speed - 1) // speed

        return hours

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            hours = self.calculateHours(piles, mid)

            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans