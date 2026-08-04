# Solution 1 (Time Complexity: O(n²), Space Complexity: O(1))
# Uses two nested loops to compare every possible pair of numbers.
# The second loop starts from the next index (i + 1) to avoid checking 
# the same pair twice or comparing an element with itself.

# Note:
# - Simple and easy to understand.
# - Not efficient for large inputs because every pair is checked.

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



# Solution 2 (Time Complexity: O(n), Space Complexity: O(n))
# Uses a hash map (dictionary) to store previously visited numbers
# along with their indices. For each number, calculate the required
# complement (target - current number) and check if it has already
# been seen.

# Note:
# - More efficient because the array is traversed only once.
# - Dictionary lookups take O(1) average time, making this the
#   preferred solution for this problem.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, curr in enumerate(nums):
            complement = target - curr
            if complement in seen:
                return [seen[complement], i]
        
            seen[curr] = i

        return []

if __name__ == "__main__":
    s1 = Solution()
    print(f"Answer: {s1.twoSum([3, 2, 3], 6)}")