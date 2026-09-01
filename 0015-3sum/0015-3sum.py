class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # 1. Early termination: Smallest element > 0 means no triplet can sum to 0
            if nums[i] > 0:
                break

            # 2. Skip duplicates for the anchor element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 3. Early termination: Smallest possible sum with current nums[i] is > 0
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break

            # 4. Skip iteration: Largest possible sum with current nums[i] is < 0
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Advance pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res