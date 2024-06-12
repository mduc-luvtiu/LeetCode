class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(n):
                if (nums[i] + nums[j] == target) and (i != j):
                    res.append(i)
                    res.append(j)
                    return res


# test
a = Solution().twoSum([1, 2, 3, 4, 6], 7)
print(a)
