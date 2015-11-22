class Solution(object):                                         
    def getRow(self, numRows):                                
        """                                                     
        :type numRows: int                                      
        :rtype: List[List[int]]                                 
        """
        if not numRows or numRows == 1:
            return [1] if not numRows else [1, 1]
        last_row = [1, 1]
        current_row = [1, 2, 1]
        for i in range (3, numRows+1):                            
            t = [1]                                             
            for j in range(0, i-1):                             
                t.append(sum(current_row[j:j+2]))                
            t.append(1)
            last_row = current_row
            current_row = t
        return current_row                                           
