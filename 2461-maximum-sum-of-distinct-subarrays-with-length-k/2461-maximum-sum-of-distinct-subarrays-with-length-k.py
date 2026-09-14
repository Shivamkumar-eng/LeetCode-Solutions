class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        summ = 0
        distinct = 0
        count = {}

        for i, num in enumerate(nums):
            # Add the current element to the window
            summ += num
            count[num] = count.get(num, 0) + 1
            if count[num] == 1:
                distinct += 1

            # Shrink window from the left if it exceeds size k
            if i >= k:
                left_num = nums[i - k]
                summ -= left_num
                count[left_num] -= 1
                if count[left_num] == 0:
                    distinct -= 1

            # Update maximum sum if the window size is k and all elements are distinct
            if i >= k - 1 and distinct == k:
                ans = max(ans, summ)

        return ans