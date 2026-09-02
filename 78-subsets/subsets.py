class Solution:
    def subsets(self, nums):
        result = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Don't include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return result