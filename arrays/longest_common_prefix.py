# Solution 1 (Time Complexity: O(n × m), Space Complexity: O(1))
# Starts with the first string as the prefix and keeps shortening it
# until it becomes the prefix of every other string.

# Note:
# - Easy to understand and implement.
# - Efficient because the prefix is only shortened when necessary.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


if __name__ == "__main__":
    s1 = Solution
    print(f"{s1.longestCommonPrefix(s1, ['flower', 'flow', 'flight'])}")
    print(f"{s1.longestCommonPrefix(s1, ['dog', 'racecar', 'car'])}")




# Solution 2 (Time Complexity: O(n × m), Space Complexity: O(1))
# Compares each character of the first string with the characters
# at the same position in the remaining strings.

# Note:
# - Stops immediately when a mismatch is found.
# - Simple approach that works well without using extra space.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i, ch in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return strs[0][:i]
        return strs[0]




# Solution 3 (Time Complexity: O(n × m), Space Complexity: O(1))
# Uses a while loop to compare characters at the same index across
# all strings and builds the common prefix one character at a time.

# Note:
# - Similar to Solution 2 but builds the answer incrementally.
# - Returns as soon as a mismatch or the end of a word is reached.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        common = ""
        i = 0

        while i < len(strs[0]):
            ch = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != ch:
                    return common

            common += ch
            i += 1

        return common
