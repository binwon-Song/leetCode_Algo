class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # sol) floyd Warshall
        n=len(graph)
#         result_table=[[inf for i in range(len_graph)] for i in range(len_graph)]
#         row=0
#         for source in graph:
#             for dest in source:
#                 result_table[row][dest]=1
#                 result_table[dest][row]=1
#             row+=1
#         for i in range(len_graph):
#             result_table[i][i]=0
        
#         print(result_table)
#         print("=========================")
#         for k in range(len_graph):
#             for i in range(len_graph):
#                 for j in range(len_graph):
#                     if result_table[i][k]+ result_table[k][i]<result_table[i][j]:
#                         result_table[i][j]=result_table[i][k]+result_table[k][j]
#         print(result_table)

#         # sol2) dfs
    
#         def dfs(start, visited=None):
#             cnt=0
#             if visited is None:
#                 visited = [False] * len(graph)  # Initialize the visited list only when it's None
#             visited[start] = True
#             print(start,visited)
#             cnt+=1
#             for neighbor in graph[start]:
#                 if not visited[neighbor]:
#                     dfs(neighbor, visited)
#                     cnt+=1
#                     print(start,visited)
#                 if all(visited):
#                     print("==========",start,visited)
#                     result.append(cnt)
#             return visited
#         result=[]
#         dfs(0)
#         print(result)


        # Initialize traversal queue
        # parameter of tuple: (node idx, state mask, visiting path length)
        traversal_queue = deque( [(node_idx, 1 << node_idx , 0) for node_idx in range(n) ] )

        # parameter of visited tuple: (node index, search state mask)
        visited = { (node_idx, 1 << node_idx ) for node_idx in range(n) }

        # Mask of all node visited
        all_node_visited = (1 << n) - 1

        # Launch BFS traversal from each node in graph G as source
        while traversal_queue:

            cur_node, cur_state, path_length = traversal_queue.popleft()

            # We've visited all nodes in graph G at least once
            if cur_state == all_node_visited:
                return path_length
            
            # Visit neighbor of current node
            for neighbor_idx in graph[cur_node]:

                next_state = cur_state | (1 << neighbor_idx)
                next_length = path_length + 1

                # If pair (neighbor index, next state) is not seen before
                if (neighbor_idx, next_state) not in visited:

                    traversal_queue.append( (neighbor_idx, next_state, next_length) )
                    visited.add( (neighbor_idx, next_state) )

        
        return -1
                    
        