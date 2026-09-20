class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)
        left_product = [1] * (size + 2)
        right_product = [1] * (size + 2)
        for i in range(size):
            left_product[i+1] = nums[i] * left_product[i]
            right_product[size - i] = nums[size - i - 1] * right_product[size - i + 1]
        
        answer = [i] * (size)
        for i in range(size):
            answer[i] = left_product[i] * right_product[i+2]
        return answer
        