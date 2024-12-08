def binary_search(nums, n):
    left = 0
    right = len(nums) - 1
    middle = 0

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == n:
            return middle
        if nums[middle] > n:
            right = middle - 1
        else:
            left = middle + 1

    return -1


# Tests for "binary_search" function

test_list = [1, 3, 5, 7, 9, 11, 13, 15]

assert binary_search(test_list, 7) != -1, "Should find existing number"

assert binary_search(test_list, 4) == -1, "Should return -1 for non-existing number"

assert binary_search([], 5) == -1, "Should handle empty list"

assert binary_search(test_list, 1) != -1, "Should find first element"
assert binary_search(test_list, 15) != -1, "Should find last element"

print("\033[92mAll test cases passed!\033[0m")

# ---------------------------------------- #

# Solution to the leetcode binary sarch problem:


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        middle = 0

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1
