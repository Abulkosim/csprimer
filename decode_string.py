class Solution(object):
    def decodeString(self, s):
        stack = []
        cur_num = 0
        cur_string = ""
        for c in s:
            if c == "[":
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ""
                cur_num = 0
            elif c == "]":
                num = stack.pop()
                prevString = stack.pop()
                cur_string = prevString + num * cur_string
            elif c.isdigit():
                cur_num = int(c)
            else:
                cur_string += c
        return cur_string


solution = Solution()
print(solution.decodeString("3[a]2[bc]"))
