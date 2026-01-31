class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        boxes=[set() for i in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    num=board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3)*3+(c//3)].add(num)
        def bt(r,c):
            if r==9:
                return True
            if c==9:
                return bt(r+1,0)
            if board[r][c]!=".":
                return bt(r,c+1)
            boxid=(r//3)*3+(c//3)
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[boxid]:
                    board[r][c]=num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[boxid].add(num)
                    if bt(r,c+1):
                        return True
                    board[r][c]="."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[boxid].remove(num)
            return False
        bt(0,0)
