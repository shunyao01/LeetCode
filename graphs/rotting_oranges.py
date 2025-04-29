from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Return minimum number of minutes until all oranges become rotten, else return 1 if impossible

        Args:
            grid: a list of list recording the status of oranges in the squares, 0:empty, 1:fresh, 2:rotten

        Return:
            integer: number of minutes until all oranges becone rotten
        
        Time complexity: O(n * m)
        Space complexity: O(n * m) 
        
        Trick: Multi source BFS

        Queue contains tuple index, visited use tuple index as key
        How to start multi source? Start with all rotten orange in start 
        How to count time? keep track when every round pass, tuple (i,j,time) vs count len(q) finish for each round
        How to track fresh? when fresh oranges finish and 
        No need visited, as we only track fresh orange = 1
        """
        m, n = len(grid), len(grid[0])
        time = 0
        fresh = 0
        queue = []

        # starting phase: add all rotten oranges to q
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh>0:
            for _ in range(len(queue)):
                # set visited
                i, j = queue.pop(0)

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    # check top bot left right
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]==1: # if valid and met fresh orange
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        fresh -= 1
            time += 1   

        return time if fresh == 0 else -1