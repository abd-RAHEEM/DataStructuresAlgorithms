class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stk=[]
        score=0
        for i in range(len(operations)):
            if operations[i]=='C':
                stk.pop()
            elif operations[i]=='D':
                stk.append((stk[-1])*2)
            elif operations[i]=='+':
                stk.append(stk[-1]+stk[-2])
            else:
                stk.append(int(operations[i]))
        for i in stk:
            score+=i
        return score
            