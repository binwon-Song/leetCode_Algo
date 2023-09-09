class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # allow duplication, make the target number using given array
        # then return the possible combination
        
        # sol 1) how to represent target number to given array numbers
        nums.sort()
        dp = [0] * (target+1)
        
        for curr in range(target+1):
            for num in nums:
                if num > curr: break
                elif num == curr: dp[curr] += 1
                else: dp[curr] += dp[curr - num]
        print(dp)
        return dp[target]
        