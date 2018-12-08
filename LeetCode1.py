class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 第一种（比较耗时）
        # for index, value in enumerate(nums):
        #     for index1 in range(index+1, len(nums)):
        #         if value+nums[index1] == target:
        #             return index, index1
        
        # 第二种
        for num in nums:
            num1 = target - num
            if num != num1 and num1 in nums:
                return [nums.index(num), nums.index(num1)]
            if num == num1 and nums.count(num) > 1:
                return [i for i,v in enumerate(nums) if v == num]
        return None