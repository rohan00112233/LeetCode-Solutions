class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],nums[i]+dp[i-1])

        return max(dp)


        # n= len(nums)
        # curr_sum = 0
        # max_sum = nums[0]
        # for i in range(n):
        #     curr_sum += nums[i]
        #     if curr_sum > max_sum:
        #         max_sum = curr_sum
        #     if curr_sum<0:
        #         curr_sum =0
        
        # return max_sum
        