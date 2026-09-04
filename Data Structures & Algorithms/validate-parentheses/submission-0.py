class Solution:
    def isValid(self, s: str) -> bool:
        brackStack = []
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        for c in s:
            if c in opening:
                brackStack.append(c)
            elif c in closing:
                if not brackStack:
                    return False
                top = brackStack.pop()
                if opening.index(top) != closing.index(c):
                    return False
        return len(brackStack) == 0