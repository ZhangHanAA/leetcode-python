class Solution:

    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            v = target - nums[i]
            for j in range(n):
                if v == nums[j] and i != j:
                    return i, j


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)
