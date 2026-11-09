class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        l = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in l:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
            
            if token == "-":
                stack.append(int(a - b))
            elif token == "+":
                stack.append(int(a + b))
            elif token == "*":
                stack.append(int(a * b))
            elif token == "/":
                stack.append(int(a/b))
        
        return stack.pop()