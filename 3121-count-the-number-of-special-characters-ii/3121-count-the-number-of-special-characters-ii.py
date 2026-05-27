class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Maps to store the last position of lowercase and first position of uppercase
        # Initialize with -1 to indicate "not seen yet"
        last_lower = [-1] * 26
        first_upper = [-1] * 26
        
        # Track characters that violated the rule (lowercase after uppercase)
        invalidated = [False] * 26

        for i, char in enumerate(word):
            if char.islower():
                idx = ord(char) - ord('a')
                last_lower[idx] = i
                # If we've already seen an uppercase version, this lowercase appearance violates the rule
                if first_upper[idx] != -1:
                    invalidated[idx] = True
            else:
                idx = ord(char) - ord('A')
                # We only care about the FIRST occurrence of the uppercase letter
                if first_upper[idx] == -1:
                    first_upper[idx] = i

        # Count how many characters satisfy all rules
        special_count = 0
        for i in range(26):
            # 1. Must have both lowercase and uppercase forms
            # 2. Every lowercase must be before the first uppercase
            # 3. Must not be invalidated by a late lowercase appearance
            if last_lower[i] != -1 and first_upper[i] != -1:
                if last_lower[i] < first_upper[i] and not invalidated[i]:
                    special_count += 1

        return special_count