# Solution 1 (Time Complexity: O(log n), Space Complexity: O(1))
# Uses binary search to find the target or the position where it
# should be inserted in the sorted array.

# Note:
# - Efficient because the search range is cut in half after each step.
# - If the target is not found, l points to the correct insert position.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        mid = (l + h)//2
        while(l <= h):
            if(nums[mid] == target):
                return(mid)
            elif(nums[mid] > target):
                h = mid-1
                mid = (l + h)//2
            else:
                l = mid+1
                mid = (l + h)//2
        return(l)


if __name__ == "__main__":
    s1 = Solution
    print(f"Index: {s1.searchInsert(s1, [1,3,5,6], 5)}")
    print(f"Index: {s1.searchInsert(s1, [1,3,5,6], 2)}")