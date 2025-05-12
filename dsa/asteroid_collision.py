class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            while True:
                if not stack:
                    stack.append(asteroid)
                    break

                popped_asteroid = stack.pop()

                if popped_asteroid * asteroid > 0:
                    stack.append(popped_asteroid)
                    stack.append(asteroid)
                    break

                if popped_asteroid > 0 and asteroid < 0:
                    if abs(popped_asteroid) > abs(asteroid):
                        stack.append(popped_asteroid)
                        break
                    elif abs(popped_asteroid) < abs(asteroid):
                        continue
                    else:
                        break
                else:
                    stack.append(popped_asteroid)
                    stack.append(asteroid)
                    break

        return stack


solution = Solution()

test_cases = [
    ([10, 2, -5], [10]),
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),
]

for i, (input_arr, expected) in enumerate(test_cases):
    result = solution.asteroidCollision(input_arr)
    print(f"Input: {input_arr}")
    print(f"Expected: {expected}")
    print(f"Output: {result}")
    print(f"{'Passed' if result == expected else 'Failed'}\n")
