class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            # Opening bracket: push onto stack
            if c not in pairs:
                stack.append(c)

            # Closing bracket: check for a match
            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != pairs[c]:
                    return False

        return not stack