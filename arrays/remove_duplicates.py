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
