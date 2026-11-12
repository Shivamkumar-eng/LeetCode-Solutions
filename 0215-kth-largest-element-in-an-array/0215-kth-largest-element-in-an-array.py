import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = []

        for num in nums:
            heapq.heappush(h, num)

            if len(h) > k:
                heapq.heappop(h)

        return h[0]