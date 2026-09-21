class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for i in s:
            if i in map:
                stack.append(i)
            else:
                if not stack:
                    return False

                if map[stack[-1]] == i:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0