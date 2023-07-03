class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s=list(s)
        goal=list(goal)
        cnt=0
        set_s=set(s)
        s_len=len(s)
        k=[]
        
        if s_len!=len(goal):
            return False
        if s==goal:
            return len(set_s)<len(goal)
        
        # for i in range(s_len):
        #     if s[i]!=goal[i]:
        #         k[i]=ord(s[i])-ord(goal[i])
        sum=0
        for i in range(s_len):
            if s[i]!=goal[i]:
                k.append(i)
                if len(k)>2:
                    return False
        print("Retn",k)
        return len(k)==2 and s[k[0]]==goal[k[1]] and s[k[1]]==goal[k[0]]
        
#         def buddyStrings(self, s: str, goal: str) -> bool:
#         ns = len(s)
#         ng = len(goal)

#         if ns != ng:
#             return False

#         if s == goal:
#             farr = [0] * 26
#             for ch in s:
#                 farr[ord(ch) - ord('a')] += 1
            
#             for count in farr:
#                 if count > 1:
#                     return True
            
#             return False

#         ans = []
#         for i in range(ns):
#             if s[i] != goal[i]:
#                 ans.append(i)
#                 if len(ans) > 2:
#                     return False

#         return len(ans) == 2 and s[ans[0]] == goal[ans[1]] 
#                   and s[ans[1]] == goal[ans[0]]