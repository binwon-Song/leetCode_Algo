class Solution:
    def check_top2btn(self,limit_y,limit_x,cells,day):
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        start_arr=[[0]*limit_x for _ in range(limit_y)]
        for row,col in cells[:day]:
            start_arr[row-1][col-1]=1
            
        def dfs(row,col):
                
                if row<0 or row>=limit_y or col<0 or col>=limit_x or start_arr[row][col]!=0:
                    return False
                
                if row==limit_y-1:
                    return True
                start_arr[row][col]=-1
                for i in range(4):
                    if dfs(row+dy[i],col+dx[i]):
                        return True
                return False
            
        for i in range(limit_x):
            if start_arr[0][i]==0 and dfs(0,i):
                return True
        return False

    
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left,right=1,row*col
        # 도달 못할 경우의 수
        # 1. top, bottom 전체 1
        # 2. 4방 중 3방(왼,오,아래)이 막혀있을 경우 -> 다음 row th
        while left<right:
            mid=right-(right-left)//2
            if self.check_top2btn(row,col,cells,mid):
                left=mid
            else:
                right=mid-1
        return left            
            
