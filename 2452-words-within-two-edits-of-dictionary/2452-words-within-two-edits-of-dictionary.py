class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        ans = []
        
        for query in queries:
            for word in dictionary:
                # Count mismatches between query and dictionary word
                diffs = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        diffs += 1
                    
                    # Optimization: if we exceed 2 edits, stop checking this word
                    if diffs > 2:
                        break
                
                # If we found a match within 2 edits, add to answer and move to next query
                if diffs <= 2:
                    ans.append(query)
                    break
        
        return ans