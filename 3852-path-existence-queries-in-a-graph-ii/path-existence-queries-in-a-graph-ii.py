class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        vals = sorted(list(set(nums)))
        m = len(vals)
        
        # Step 2: Initialize binary lifting table
        # 18 levels are enough since 2^17 = 131,072 > 10^5
        max_levels = 18
        go_right = [[0] * m for _ in range(max_levels)]
        
        # Compute the furthest index reachable in 1 step for each value
        for i in range(m):
            # bisect_right finds the first element strictly greater than the target.
            # Subtracting 1 gives the index of the largest element <= vals[i] + maxDiff
            it = bisect.bisect_right(vals, vals[i] + maxDiff)
            go_right[0][i] = it - 1
            
        # Fill the binary lifting table
        for k in range(1, max_levels):
            for i in range(m):
                go_right[k][i] = go_right[k - 1][go_right[k - 1][i]]
                
        # Step 3: Answer each query
        ans = []
        for u, v in queries:
            # Case 1: Same node
            if u == v:
                ans.append(0)
                continue
                
            # Case 2: Different nodes but have the exact same value
            if nums[u] == nums[v]:
                ans.append(1)
                continue
                
            # Find positions in the sorted unique values array
            idx_u = bisect.bisect_left(vals, nums[u])
            idx_v = bisect.bisect_left(vals, nums[v])
            
            # Since the graph is undirected, we always move left-to-right
            if idx_u > idx_v:
                idx_u, idx_v = idx_v, idx_u
                
            # If the maximum possible reach from u cannot even touch v, they are disconnected
            if go_right[max_levels - 1][idx_u] < idx_v:
                ans.append(-1)
                continue
                
            # Binary lifting to find the minimum steps
            steps = 0
            curr = idx_u
            for k in range(max_levels - 1, -1, -1):
                # If a jump of 2^k steps doesn't reach or pass the target, take the jump
                if go_right[k][curr] < idx_v:
                    steps += (1 << k)
                    curr = go_right[k][curr]
                    
            # One final step is needed to bridge the remaining gap to idx_v
            ans.append(steps + 1)
            
        return ans
        