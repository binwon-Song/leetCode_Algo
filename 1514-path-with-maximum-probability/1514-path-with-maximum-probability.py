from collections import deque
class Solution:
    
    def bfs(self,start:int,end:int,graph,table):
        que=deque()
        que.append(start)
        # bfs start
        while que:
            cur_vertex=que.popleft()
            for node,prob in graph[cur_vertex]:
                new_prob=table[cur_vertex]*prob
                if new_prob>table[node]:
                    table[node]=new_prob
                    que.append(node)
        return table
            
    
        
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], 
                       start: int, end: int) -> float:
        # star to end max cost
        # if start to end no way -> return 0
        # careful float
        
        graph=[[] for i in range(n)]
        
        i=0        
        # create undir graph with cost
        for st,dt in edges:
            graph[st].append([dt,succProb[i]])
            graph[dt].append([st,succProb[i]])
            i+=1
            
        table=[0.0]*n
        table[start]=1.0
        table=self.bfs(start,end,graph,table)
        print(table)
        return table[end]
    
        