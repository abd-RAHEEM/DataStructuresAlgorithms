class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        
        # Each node stores: (prefix_len, suffix_len, max_len, segment_len, left_char, right_char)
        tree = [None] * (4 * n)
        
        def merge(left, right):
            lp, ls, lm, llen, lc_left, rc_left = left
            rp, rs, rm, rlen, lc_right, rc_right = right
            
            # Default merged values
            new_lp = lp
            new_rs = rs
            new_lm = max(lm, rm)
            new_len = llen + rlen
            
            # Check if boundary characters match
            if rc_left == lc_right:
                new_lm = max(new_lm, ls + rp)
                
                # If left segment is all same character, extend prefix
                if lp == llen:
                    new_lp = llen + rp
                
                # If right segment is all same character, extend suffix
                if rs == rlen:
                    new_rs = rlen + ls
                    
            return (new_lp, new_rs, new_lm, new_len, lc_left, rc_right)

        def build(u, l, r):
            if l == r:
                tree[u] = (1, 1, 1, 1, s[l], s[l])
                return
            
            mid = (l + r) // 2
            build(u * 2, l, mid)
            build(u * 2 + 1, mid + 1, r)
            tree[u] = merge(tree[u * 2], tree[u * 2 + 1])

        def update(u, l, r, pos, c):
            if l == r:
                s[pos] = c
                tree[u] = (1, 1, 1, 1, c, c)
                return
            
            mid = (l + r) // 2
            if pos <= mid:
                update(u * 2, l, mid, pos, c)
            else:
                update(u * 2 + 1, mid + 1, r, pos, c)
            
            tree[u] = merge(tree[u * 2], tree[u * 2 + 1])

        build(1, 0, n - 1)
        ans = []
        
        for pos, c in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, pos, c)
            # The 3rd element in the root tuple represents the global maximum length
            ans.append(tree[1][2])
            
        return ans