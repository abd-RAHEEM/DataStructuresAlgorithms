import collections

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # 1. Build adjacency list
        adj = collections.defaultdict(list)
        for fr, t, pr in flights:
            adj[fr].append((t, pr))
            
        # 2. Track the minimum cost to reach each node
        prices = [float('inf')] * n
        prices[src] = 0
        
        # 3. Standard BFS queue: stores (node, current_total_price)
        q = collections.deque([(src, 0)])
        stops = 0
        
        # Loop until we exhaust k stops or the queue runs dry
        while q and stops <= k:
            size = len(q)
            for _ in range(size):
                node, cur_price = q.popleft()
                
                for neigh, pr in adj[node]:
                    new_price = cur_price + pr
                    
                    # Only push to queue if this path offers a cheaper 
                    # way to reach 'neigh' within the current number of stops
                    if new_price < prices[neigh]:
                        prices[neigh] = new_price
                        q.append((neigh, new_price))
            stops += 1
            
        return prices[dst] if prices[dst] != float('inf') else -1