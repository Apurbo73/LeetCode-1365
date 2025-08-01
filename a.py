class Solution:
    def smallerNumbersThanCurrent(self, nums):
        dic = {}
        ans = []
        sorted_num = sorted(nums)

        for i in range(len(sorted_num)):
            if sorted_num[i] not in dic:
                dic[sorted_num[i]] = i

        for num in nums:
            ans.append(dic[num])

        return ans
