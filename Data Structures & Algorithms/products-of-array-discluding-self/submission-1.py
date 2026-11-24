class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Multiply products to the LEFT of i
        left_product = 1
        for i in range(n):
            # Save the current left_product into our memory (answer array)
            answer[i] = left_product
            # Update left_product for the next index
            left_product *= nums[i]
            
        # Multiply products to the RIGHT of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            # Multiply what we remembered from the left by the right_product
            answer[i] *= right_product
            # Update right_product for the next index (moving left)
            right_product *= nums[i]
            
        return answer