# Solution (Time Complexity: O(n²), Space Complexity: O(n²))
# Builds each row of Pascal's Triangle using the values from the
# previous row. The first and last values of each row remain 1.
# Note:
# - Each inner value is calculated by adding the two values above it.
# - Stores the complete triangle in final.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        final = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = final[i - 1][j - 1] + final[i - 1][j]

            final.append(row)

        return final
