class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        # Product of everything to the left
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        # Product of everything to the right
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result