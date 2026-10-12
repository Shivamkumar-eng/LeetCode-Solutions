
class Solution:
    def count(self, weights, mid):
        Total = 0
        hours = 1

        for i in range(len(weights)):
            if Total + weights[i] <= mid:
                Total += weights[i]
            else:
                Total = weights[i]
                hours += 1

        return hours

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        maximum = 0
        for j in range(len(weights)):
            maximum += weights[j]

        left = max(weights)
        right = maximum

        while left <= right:
            mid = left + (right - left) // 2
            Total_hours = self.count(weights, mid)

            if Total_hours <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left