# Last updated: 7/27/2026, 4:14:10 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_cities = len(isConnected)
        parent = [i for i in range(num_cities)]
        provinces = num_cities

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            nonlocal provinces
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_i] = root_j
                provinces -=1

        for i in range(num_cities):
            for j in range(i+1,num_cities):
                if isConnected[i][j] == 1:
                    union(i,j)

        return provinces        
            