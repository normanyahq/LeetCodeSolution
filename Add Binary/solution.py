class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        if len(a) < len(b):
            a, b = b, a
        add = False
        for i in range(0, len(a)):
            a_bit = a[len(a)-i-1] == '1'
            b_bit = b[len(b)-i-1] == '1' if i<len(b) else 0
            result = ('1' if (a_bit ^ b_bit ^ add) else '0') + result
            add = (a_bit + b_bit + add) > 1
        if add:
            result = '1' + result
        return result
            
