# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         if len(s) == 0:
#             return
#         # print("A",s)
#         self.reverseString(s[0:len(s)-1])
#         print(tmp)
        
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(l, r, s):
            if l >= r:
                return s
            s[l], s[r] = s[r], s[l]        
            return helper(l+1, r-1, s)
        helper(0, len(s)-1, s)            