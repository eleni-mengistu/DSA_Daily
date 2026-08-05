# Solution (Time Complexity: O(n), Space Complexity: O(1))
# Starts from the last digit and moves backwards. If the digit is 9,
# it becomes 0 and the carry moves to the previous digit. Otherwise,
# the digit is increased by 1 and the result is returned.

# Note:
# - Handles cases with multiple 9s, such as [9, 9, 9].
# - Only adds a new digit when all digits are 9.


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits

            digits[i] = 0
            # print(f"Digits before insertion: {digits}")

        digits.insert(0, 1)
        # print(f"Digits after insertion: {digits}")
        return digits

if __name__ == "__main__":
    s1 = Solution
    print(f"{s1.plusOne(s1, [1,2,3])}")
    print(f"{s1.plusOne(s1, [9])}")
    print(f"{s1.plusOne(s1, [3, 9, 9, 9])}")