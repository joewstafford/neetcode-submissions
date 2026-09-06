class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = {"*", "+", "-", "/"}
        stack = []
        for c in tokens:
            if c not in symbols:
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    result = a + b
                elif c == "-":
                    result = a - b
                elif c == "*":
                    result = a * b
                else:
                    result = int(a / b)
                stack.append(result)
        return stack[0]            

        