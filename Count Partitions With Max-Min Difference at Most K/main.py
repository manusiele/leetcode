class Solution(object):
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        prefix = [0] * (n + 2)
        prefix[1] = 1
        
        left = 0
        min_deq = deque()
        max_deq = deque()
        
        for i in range(n):
            # Maintain max deque
            while max_deq and nums[max_deq[-1]] <= nums[i]:
                max_deq.pop()
            max_deq.append(i)
            
            # Maintain min deque
            while min_deq and nums[min_deq[-1]] >= nums[i]:
                min_deq.pop()
            min_deq.append(i)
            
            # Shrink window
            while left <= i and nums[max_deq[0]] - nums[min_deq[0]] > k:
                if max_deq[0] == left:
                    max_deq.popleft()
                if min_deq[0] == left:
                    min_deq.popleft()
                left += 1
            
            # Add all valid ways
            dp[i+1] = (prefix[i+1] - prefix[left] + MOD) % MOD
            prefix[i+2] = (prefix[i+1] + dp[i+1]) % MOD
        
        return dp[n]