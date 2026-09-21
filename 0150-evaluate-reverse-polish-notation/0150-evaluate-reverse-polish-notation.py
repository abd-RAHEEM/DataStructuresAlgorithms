class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators=['+','-','*','/']
        stack=[]
        
        for tok in tokens:
            if tok in operators:
                a=stack.pop()
                b=stack.pop()
                if tok =='+':
                    stack.append(b+a)
                elif tok=='-':
                    stack.append(b-a)
                elif tok=='*':
                    stack.append(b*a)
                else:
                    stack.append(int(float(b)/a))
            else:
                stack.append(int(tok))
        return stack.pop()


        