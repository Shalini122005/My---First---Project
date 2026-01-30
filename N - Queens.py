class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for i in range(n)]
        res=[]
        def issafe(r,c,board):
            #upper row
            for i in range(r-1,-1,-1):
                if board[i][c]=='Q':
                    return False
            row,col=r-1,c-1
            while row>-1 and col>-1:
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1
            row,col=r-1,c+1
            while row>-1 and col<n:
                if board[row][col]=='Q':
                    return False
                row-=1
                col+=1
            return True
        def bt(row,n,board,res):
            if row==n:
                res.append(["".join(row) for row in board])
                return 
            for col in range(n):
                if issafe(row,col,board):
                    board[row][col]='Q'
                    bt(row+1,n,board,res)
                    board[row][col]='.'
        bt(0,n,board,res)
        return res
