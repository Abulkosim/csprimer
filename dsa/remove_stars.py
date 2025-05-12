class Solution:
    def removeStars(self, s: str) -> str:
        result = []

        for char in s:
            if char != "*":
                result.append(char)
            else:
                result.pop()

        return "".join(result)


solution = Solution()
# Test cases
assert solution.removeStars("leet**cod*e") == "lecoe"
assert solution.removeStars("erase*****") == ""
assert solution.removeStars("abc*def*") == "abde"
assert solution.removeStars("") == ""
assert solution.removeStars("a*b*c*") == ""
assert solution.removeStars("hello") == "hello"

print("All test cases passed!")

solution.removeStars("leet**cod*e")
