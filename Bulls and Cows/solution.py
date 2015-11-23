class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        sec, gue  = {}, {}
        for i, j in zip(secret, guess):
            bull += i==j
            if i != j:
                sec[i] = sec.get(i, 0) + 1
                gue[j] = gue.get(j, 0) + 1
        for k in sec:
            cow += min (sec[k], gue.get(k, 0))
        return "%dA%dB" %(bull, cow)
