from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Return the distance of the nearest 0 for each cell

        Args:
            mat: list of list of integers with 0s and 1s

        Return:
            liist of list of integer which are the distances

        Time Complexity: O(mn)
        Space Complexity: O(mn)

        Multi-source BFS or 2 Pass Dynamic Programming
        """
        q = deque()

        # add all zeros as starting points
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0: 
                    q.append((i, j))
                else:
                    mat[i][j] = math.inf

        # traverse
        while q:
            for _ in range(len(q)): # phase by phase
                i, j = q.popleft()
                for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]: # explore neighbor
                    if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]) and mat[ni][nj] == math.inf: # check valid nb
                        q.append((ni, nj))
                        mat[ni][nj] = mat[i][j] + 1 # it must be a newly explored 1

        return mat

        # 2 pass dp
        # m, n = len(mat), len(mat[0])
        # dist = [[float('inf')] * n for _ in range(m)]

        # # First pass: top-left to bottom-right
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == 0:
        #             dist[i][j] = 0
        #         else:
        #             if i > 0:
        #                 dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
        #             if j > 0:
        #                 dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

        # # Second pass: bottom-right to top-left
        # for i in reversed(range(m)):
        #     for j in reversed(range(n)):
        #         if i < m - 1:
        #             dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
        #         if j < n - 1:
        #             dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)

        # return dist