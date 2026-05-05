class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create sets to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate through each cell
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                # Skip empty cells
                if num == '.':
                    continue
                
                # Calculate which 3x3 box this cell belongs to
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if number already exists in row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                # Add number to respective sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        return True
