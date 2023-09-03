class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 로봇은 0,0이 시작점
        # 로봇은 오른쪽 또는 아래 쪽으로만 이동 가능
        # m x n 그리드가 주어짐.
        # unique 경로의 가짓 수 찾기
        
        # solution 1 => DP
        dp=[[1 for j in range(n)] for i in range(m)]
        # calcu unique path 
        for col in range(1,m):
            for row in range(1,n):
                dp[col][row]=dp[col-1][row]+dp[col][row-1]
        return dp[m-1][n-1]
    