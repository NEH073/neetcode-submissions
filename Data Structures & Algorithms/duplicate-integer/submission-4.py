class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = set()
        for num in range(len(nums)):
            if nums[num] in appear:
                return True
            appear.add(nums[num])
        return False   