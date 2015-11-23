class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S1 = (C-A) * (D-B) 
        S2 = (G-E) * (H-F)
        
        if E>=C or F>=D or B>=H or A>=G: # no shared area
            S_shared = 0
        else: 
            S_shared = (min(G, C) - max(A, E)) * (min(H,D) - max(F, B))
        return S1 + S2 - S_shared
