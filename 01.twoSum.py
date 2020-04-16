"""
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。
你可以假设每种输入只对应一个答案，但是，数组中的同一个元素不能使用两遍。

"""


def twoSum(nums, target):
    """
    O(n2)的方法.
    """
    n = len(nums)
    for i in range(n):
        v = target - nums[i]
        for j in range(n):
            if v == nums[j] and i != j:
                return i, j


def twoSum2(nums, target):
    """
    O(n)的方法，遍历两次，但需要字典记录出现的位置，需要额外O(n)的空间
    """
    have = {}
    for i in range(len(nums)):
        have[nums[i]] = i
    for i in range(len(nums)):
        v = target - nums[i]
        if v in have.keys() and have[v] != i:
            return i, have[v]


def twoSum3(nums, target):
    """
    遍历一遍的方法
    """
    have = {}
    for i in range(len(nums)):

        v = target - nums[i]
        if v in have.keys():
            return have[v], i

        have[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
    print(twoSum2(nums, target))
    print(twoSum3(nums, target))

    nums = [1, 3, 4, 2, 3, 5, 9]
    target = 10
    print(twoSum(nums, target))
    print(twoSum2(nums, target))
    print(twoSum3(nums, target))
