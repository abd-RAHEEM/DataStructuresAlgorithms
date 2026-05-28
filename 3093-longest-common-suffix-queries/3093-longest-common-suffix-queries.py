class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the index of the best word passing through / ending at this node
        self.best_index = -1 

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        root = TrieNode()
        
        # Helper to determine if word 'i' is a better fit than word 'j'
        def is_better(i, j):
            if j == -1:
                return True
            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return True
            if len(wordsContainer[i]) > len(wordsContainer[j]):
                return False
            return i < j  # Tie-breaker: earlier index in wordsContainer

        # 1. Build the Trie with reversed words from wordsContainer
        for idx, word in enumerate(wordsContainer):
            curr = root
            # Update the root node's default best index
            if is_better(idx, curr.best_index):
                curr.best_index = idx
                
            # Insert characters backwards
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # Update the best index for this prefix node
                if is_better(idx, curr.best_index):
                    curr.best_index = idx
                    
        # 2. Process each query
        ans = []
        for query in wordsQuery:
            curr = root
            # Traverse backwards matching the suffix
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            # The node we land on contains the index of the best matching suffix word
            ans.append(curr.best_index)
            
        return ans