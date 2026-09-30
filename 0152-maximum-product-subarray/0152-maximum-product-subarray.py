class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = float('-inf')
        
        # 1. Forward Pass (Your exact logic)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            max_product = max(product, max_product)
            if product == 0:
                product = 1
                
        # 2. Backward Pass (Fixes the odd-negative problem)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            max_product = max(product, max_product)
            if product == 0:
                product = 1
                
        return max_product
