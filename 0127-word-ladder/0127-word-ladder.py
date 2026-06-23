class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
    
        if endWord not in wordList:
            return 0
        queue=deque([(beginWord,1)])
        n=len(beginWord)
        wordset=set(wordList)
        visited={beginWord}
        while queue:
            cur,count=queue.popleft()
            if cur==endWord:
                return count
            for i in range(n):
                for char in string.ascii_lowercase:
                    if cur[i]!=char:
                        c2=cur[:i]+char+cur[i+1:]
                        if c2 in wordset and c2 not in visited:
                            queue.append((c2,count+1))
                            visited.add(c2)
        
        return 0
        