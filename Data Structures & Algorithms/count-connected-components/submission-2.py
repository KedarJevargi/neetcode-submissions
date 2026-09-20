class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [-1] * n

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x]) 
            return parent[x]

        for u, v in edges:
            ru = find(u)
            rv = find(v)

            if ru != rv:
                parent[rv] = ru

        count = 0
        for i in parent:
            if i == -1:
                count += 1

        return count