def staircase_ascent(n):
    """
    Calculate number of distinct ways to climb n stairs, taking 1 or 2 steps at a time.
    :param n: Number of stairs
    :return: Number of distinct ways to climb stairs
    """
    if n <= 1:
        return 1
    
    # Initialize array to store number of ways for each step
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case - one way to climb 0 stairs
    dp[1] = 1  # Base case - one way to climb 1 stair
    
    # Calculate ways for each step using previous results
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

# Tests for staircase_ascent function
test_cases = [
    (2, 2),    # 2 ways: 1+1, 2
    (3, 3),    # 3 ways: 1+1+1, 1+2, 2+1
    (4, 5),    # 5 ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
    (5, 8),    # 8 ways
    (0, 1),    # 1 way
    (1, 1)     # 1 way
]

for stairs, expected in test_cases:
    result = staircase_ascent(stairs)
    assert result == expected, f"For n={stairs}, expected {expected} but got {result}"

print("\033[92mAll test cases passed!\033[0m")

# Solution for leetcode climbing stairs problem:
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return staircase_ascent(n)
