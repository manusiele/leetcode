class Solution(object):
    def countPartitions(self, nums):
        total = sum(nums)
        total_parity = total % 2
        left_sum = 0
        count = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum % 2 == total_parity:
                count += 1
        return count