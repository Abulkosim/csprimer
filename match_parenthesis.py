class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {
            ')': '(',
            '}': '{', 
            ']': '['
        }
        
        for char in s:
            if char in brackets:
                top_element = stack.pop() if stack else '#'
                
                if brackets[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0


solution = Solution()
assert solution.isValid("()") == True
assert solution.isValid("()[]{}") == True
assert solution.isValid("(]") == False
assert solution.isValid("([)]") == False
assert solution.isValid("{[]}") == True
assert solution.isValid("") == True
assert solution.isValid("((") == False
assert solution.isValid("))") == False

print("\033[92mAll tests passed!\033[0m")
