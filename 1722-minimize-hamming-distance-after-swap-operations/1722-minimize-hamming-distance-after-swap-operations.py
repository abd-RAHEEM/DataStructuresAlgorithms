from collections import defaultdict, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))

        # Union-Find find function with path compression
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        # Union-Find union function
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # 1. Group all allowed swap indices
        for a, b in allowedSwaps:
            union(a, b)

        # 2. Organize source and target elements by their component root
        components = defaultdict(list)
        for i in range(n):
            root = find(i)
            components[root].append(i)

        hamming_distance = 0
        
        # 3. For each component, count how many elements can be matched
        for root in components:
            indices = components[root]
            # Count frequencies of elements in this component for both arrays
            source_counts = Counter(source[i] for i in indices)
            target_counts = Counter(target[i] for i in indices)
            
            # Intersection of counts gives the number of positions that CAN match
            matches = 0
            for val in source_counts:
                if val in target_counts:
                    matches += min(source_counts[val], target_counts[val])
            
            # Non-matches in this component contribute to the Hamming distance
            hamming_distance += (len(indices) - matches)

        return hamming_distance