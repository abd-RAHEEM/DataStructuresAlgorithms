class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        # If the last character is '1', we can never land on it
        if s[-1] == '1':
            return False
            
        n = len(s)
        dp = [False] * n
        dp[0] = True
        
        active_jumps = 0
        
        for i in range(1, n):
            # Add to our active pool if the index minJump steps behind was reachable
            if i >= minJump and dp[i - minJump]:
                active_jumps += 1
                
            # Remove from our active pool if the index maxJump + 1 steps behind falls out of our window
            if i > maxJump and dp[i - maxJump - 1]:
                active_jumps -= 1
                
            # We can reach the current index if it's a '0' AND there is at least 1 valid jump we can make
            if s[i] == '0' and active_jumps > 0:
                dp[i] = True
                
        return dp[-1]