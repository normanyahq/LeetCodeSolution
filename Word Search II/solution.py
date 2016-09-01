class TrieNode:
    def __init__(self, val):
        self.children = dict()
        self.val = val


class Trie:
    def __init__(self):
        self.root = TrieNode(False)
    def insert(self, s):
        p = self.root
        for c in s:
            if c not in p.children:
                p.children[c] = TrieNode(False)
            p = p.children[c]
        p.val = True

class Solution(object):
    
    def dfs(self, board, r, c, node, result):
        if board[r][c] not in node.children:
            return
        self.visited.add((r, c))
        dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.cur_str.append(board[r][c])
        if node.children[board[r][c]].val:
            result.add("".join(self.cur_str))
        for dr, dc in dx:
            tr, tc = dr + r, dc + c
            if tr >= 0 and tr < self.row and tc >= 0 and tc < self.col and board[tr][tc] in node.children[board[r][c]].children and (tr, tc) not in self.visited:
                self.dfs(board, tr, tc, node.children[board[r][c]], result)
        self.visited.remove((r, c))
        self.cur_str.pop()
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        tree = Trie()
        for word in words:
            tree.insert(word)
        row = len(board)
        result = set()
        col = len(board[0]) if row else 0
        self.row = row
        self.col = col
        self.cur_str = list()
        self.visited = set()
        for i in xrange(row):
            for j in xrange(col):
                self.dfs(board, i, j, tree.root, result)
        return list(result)
        
