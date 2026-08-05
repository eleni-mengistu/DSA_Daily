# Solution (Time Complexity: O(n), Space Complexity: O(1))
# Uses two pointers to keep track of the position of the next unique
# element and compare it with the previous unique element.
# Note:
# - The array is modified in place without using extra space.
# - k keeps track of the number of unique elements found.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    s1 = Solution
    print(f"{s1.removeDuplicates(s1, [1,1,2])}")
    print(f"{s1.removeDuplicates(s1, [0,0,1,1,1,2,2,3,3,4])}")
