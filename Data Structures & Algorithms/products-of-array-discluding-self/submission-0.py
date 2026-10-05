class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]* len(nums)

        preffix = 1
        for i in range(len(nums)):
            answer[i] = preffix
            preffix *= nums[i]

            suffix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer    