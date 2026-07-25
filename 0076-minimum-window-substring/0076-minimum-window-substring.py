from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        countt={}
        for c in t:
            countt[c]=1+countt.get(c,0)
        need=len(countt)
        l=0
        have=0
        window={}
        res=[-1,-1]
        reslen=float('infinity')
        for r in range(len(s)):
            char=s[r]
            window[char]=window.get(char,0)+1
            if char in countt and window[char]==countt[char]:
                have+=1
                while have==need:
                    if (r-l+1)<reslen:
                        reslen=r-l+1
                        res=[l,r]
                    window[s[l]]-=1
                    if s[l] in countt and window[s[l]]<countt[s[l]]:
                        have-=1
                    l+=1
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ""