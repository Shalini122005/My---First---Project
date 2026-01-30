class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        def bt(r,c,idx):
            if idx==len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[idx]:
                return False
            temp=board[r][c]
            board[r][c]="#"
            found=(bt(r+1,c,idx+1) or
                   bt(r-1,c,idx+1) or
                   bt(r,c+1,idx+1) or
                   bt(r,c-1,idx+1))
            board[r][c]=temp
            return found
        for i in range(rows):
            for j in range(cols):
                if bt(i,j,0):
                    return True
        return False
