class Solution:
    def productExceptSelf(self, nums):
        res = [1]*len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i-1]

        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
s= Solution()
print(s.productExceptSelf([1,2,4,6]))

