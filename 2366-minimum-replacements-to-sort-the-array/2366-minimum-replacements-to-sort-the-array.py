class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        m = inf
        ops = 0

        for n in reversed(nums): 
            if n < m:
                m = n
                continue
            d = (n-1) // m + 1   # number of summands 
            ops += d-1           # number of operations
            m = n // d           # smallest of d summands 
        
        return ops