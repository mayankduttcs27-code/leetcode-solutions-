class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []

        return [original[i * n:(i + 1) * n] for i in range(m)]