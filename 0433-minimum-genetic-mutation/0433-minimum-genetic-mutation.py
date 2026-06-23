class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1
        bank_set=set(bank)
        visited=set(startGene)
        queue=deque([(startGene,0)])
        while queue:
            gene,step=queue.popleft()
            if gene==endGene:
                return step
            for i in range(8):
                for char in ['A','C','G','T']:
                    if gene[i]!=char:
                        mutated=gene[:i]+char+gene[i+1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated,step+1))
        return -1
        
        