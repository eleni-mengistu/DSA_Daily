# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)


# Solution (Time Complexity: O(n), Space Complexity: O(1))
# Uses two pointers to move all elements that are not equal to val
# to the beginning of the array.

# Note:
# - The array is modified in place without using extra space.
# - k keeps track of the position where the next valid element is placed.
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        print(nums)
        return k

if __name__ == "__main__":
    s1 = Solution
    print(f"{s1.removeElement(s1, [3,2,2, 3], 3)}")
    print(f"{s1.removeElement(s1, [0, 1, 2, 2, 3, 0, 4, 2], 2)}")
