class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Create sets to store unique characters
        lower_chars = set()
        upper_chars = set()
        
        # Populate sets based on character case
        for char in word:
            if char.islower():
                lower_chars.add(char)
            else:
                upper_chars.add(char)
        
        # Count characters that have both cases present
        count = 0
        for char in lower_chars:
            if char.upper() in upper_chars:
                count += 1
                
        return count