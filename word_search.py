
"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        
        m, n = len(board), len(board[0])
        
        visited = set()
        
        
        def dfs(i, j, word):
            
            if not word:
                return True
            
            if i < 0 or j < 0 or i > m-1 or j > n-1 or board[i][j] != word[0] or (i,j) in visited:
                return False
            
            visited.add((i, j))
            res = dfs(i+1, j, word[1:]) or dfs(i-1, j, word[1:]) or dfs(i, j+1, word[1:]) or dfs(i, j-1, word[1:])
            visited.remove((i, j))
            return res
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        return False
            
        
                
