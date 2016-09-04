class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)
        merged = False
        if p_v != p_u:
            merged = True
        if p_u > p_v:
            self.parent[p_u] = p_v
        else:
            self.parent[p_v] = p_u
        return merged

    

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        db = UnionFind(m*n)
        matrix = [[0] * n for i in range(m)]
        dx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        mapping = lambda x, y, c: x*c + y
        set_num = 0
        result = []
        for r, c in positions:
            matrix[r][c] = 1
            set_num += 1
            for dr, dc in dx:
                tr, tc = r+dr, c+dc
                if tr>=0 and tr<m and tc>=0 and tc<n and matrix[tr][tc]:
                    set_num -= db.union(mapping(tr, tc, n), mapping(r, c, n))
            result.append(set_num)
        return result
    
