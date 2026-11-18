class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    if target - total < abs(result - target):
                        result = total
                    left += 1
                elif total > target:
                    if total - target < abs(result - target):
                        result = total
                    right -= 1
                else:
                    return total
        return result


        