class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        if not batteries:
            return 0
            
        left = 0
        right = sum(batteries) // n + 1  # upper bound: if all power used evenly
        
        def can_run_for(minutes):
            """Check if we can run all n computers for 'minutes' minutes"""
            total_available = 0
            for b in batteries:
                total_available += min(b, minutes)  # each battery contributes at most 'minutes'
                if total_available >= minutes * n:
                    return True
            return total_available >= minutes * n
        
        while left < right:
            mid = (left + right + 1) // 2  # bias towards right
            if can_run_for(mid):
                left = mid
            else:
                right = mid - 1
                
        return left