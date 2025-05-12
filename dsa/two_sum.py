class Solution(object):
    def twoSum(self, nums, target):

        map = {}

        for idx, num in enumerate(nums):
            if (target - num) in map:
                return [map[target - num], idx]
            else:
                map[num] = idx

        return []


solution = Solution()

assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([3, 3], 6) == [0, 1]

print("\033[92mAll tests passed!\033[0m")
