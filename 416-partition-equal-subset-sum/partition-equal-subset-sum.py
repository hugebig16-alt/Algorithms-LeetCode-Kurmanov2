class Solution:
    def canPartition(self, nums):
        S = sum(nums)
        if S % 2 != 0:
            return False
        
        target = S // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]