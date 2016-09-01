class Solution(object):
    def getOrder(self, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return (word1[i], word2[i])
        return None
        
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        parent = dict()
        for word in words:
            for c in word:
                parent[c] = set()
        for i in xrange(1, len(words)):
            relation = self.getOrder(words[i-1], words[i])
            if not relation:
                continue
            p, n = relation
            parent[n].add(p)
        if words:
            first_char = words[0][0]
            if len(set([w[0] for w in words])) > 1:
                for k in parent:
                    if k != first_char:
                        parent[k].add(first_char)
        result = []
        while parent:
            edge_num, k = min([(len(parent[k]), k) for k in parent])
            if edge_num:
                return ""
            for p in parent:
                parent[p].discard(k)
            del parent[k]
            result.append(k)
        return "".join(result)
