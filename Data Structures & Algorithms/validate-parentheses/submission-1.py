class Solution:
    def isValid(self, s: str) -> bool:
        brackStack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        opening = set(pairs.values())
        for c in s:
            if c in opening:
                brackStack.append(c)
            elif c in pairs:
                if not brackStack or brackStack.pop() != pairs[c]:
                    return False
        return not brackStack