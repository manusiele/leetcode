class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
            
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                board[r][c] != word[i]):
                return False
            
            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 directions
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            
            # Backtrack
            board[r][c] = temp
            return found
        
        # Try starting from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False