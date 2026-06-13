class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            # Calculate total weight for the current word
            word_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # Map the modulo result to reverse alphabetical order
            mapped_char = chr(ord('z') - (word_weight % 26))
            result.append(mapped_char)
            
        return "".join(result)