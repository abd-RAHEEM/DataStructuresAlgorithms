from collections import defaultdict, deque
import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        if endWord not in wordList:
            return []

        found = False
        wordset = set(wordList)

        parents = defaultdict(list)

        visited = {beginWord}
        queue = deque([beginWord])

        while queue and not found:

            level_set = set()

            for _ in range(len(queue)):

                word = queue.popleft()

                for i in range(len(word)):

                    for char in string.ascii_lowercase:

                        if word[i] == char:
                            continue

                        newword = word[:i] + char + word[i+1:]

                        if newword in wordset and newword not in visited:

                            if newword not in level_set:
                                queue.append(newword)
                                level_set.add(newword)

                            parents[newword].append(word)

                            if newword == endWord:
                                found = True

            visited.update(level_set)

        if not found:
            return []

        result = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return result