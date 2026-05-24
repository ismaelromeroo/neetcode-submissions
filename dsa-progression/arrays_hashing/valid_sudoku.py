"""
pattern: hash table
time: O(n^2)
space: O(1)

key insight:
the idea was to iterate through it once and utilize hashsets to identify dupilicates similar to contains
duplicates problem and similar to the other problems as well. need to view problem in terms of the topic
hashing and try to find the most effectice solution for example iterating once through a problem

mistake: took a break from these problem so forgot a bit and rushed to quickly to the solution video did break down 
or write out the problem didnt struggle on it enough need to focus on the problems more

solution:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or 
                   board[i][j] in cols[j] or 
                   board[i][j] in squares[(i//3,j//3)]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        return True
"""