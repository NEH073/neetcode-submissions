class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows =[set() for _ in range(9)]
        colums = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                curr_box =board[i][j]
                if curr_box ==".":
                    continue
        
                box_index = ((i//3)*3 + (j//3))

                if curr_box in rows[i] or curr_box in colums[j] or curr_box in boxes[box_index]:
                    return False
        
                rows[i].add(curr_box)
                colums[j].add(curr_box)
                boxes[box_index].add(curr_box)

        return True