class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        count = 0
        
        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    dfs(neigh)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count +=1
        return count 
