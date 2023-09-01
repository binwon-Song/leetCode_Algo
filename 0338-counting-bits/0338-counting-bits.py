class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans legnth -> n+1
        # ans represendted by binary each i
        # ans[i] -> nubmer of 1's
        ans=[0,]
        for i in range(1,n+1):
            ans.append((bin(i)).count('1'))
        return ans