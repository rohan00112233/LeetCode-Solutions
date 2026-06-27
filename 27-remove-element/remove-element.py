class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)
        for i in range(end):
            if nums[i]!= val:
                nums[start]=nums[i]
                start += 1
        return start        
        # for i in nums:
        #     if val in nums:
        #         nums.remove(val)
        # return len(nums)

        # k = len(nums)


        