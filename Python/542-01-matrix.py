import itertools
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        queue = []              # queue of (row, col) tuples

        for r, c in itertools.product(range(rows), range(cols)):
            if mat[r][c] == 0:
                queue.append((r,c))                                 # add all 0s to queue
            else:
                mat[r][c] = '#'                                     # mark all 1s with '#'                       


        for row, col in queue:
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:                   # check all 4 directions
                nr = row + dx
                nc = col + dy

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == '#':    # if neighbor is marked
                    mat[nr][nc] = mat[row][col] + 1
                    queue.append((nr, nc))

        return mat