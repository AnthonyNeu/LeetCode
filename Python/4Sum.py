"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                x = target - nums[i] - nums[j]
                left = j+1
                right = len(nums)-1
                while left < right:
                    if left > j + 1 and nums[left] == nums[left-1]:
                        left +=1
                        continue
                    if right < len(nums) -1 and nums[right] == nums[right+1]:
                        right -=1
                        continue
                    if nums[left] + nums[right] == x:
                        tmp = []
                        tmp.append(nums[i])
                        tmp.append(nums[j])
                        tmp.append(nums[left])
                        tmp.append(nums[right])
                        result.append(tmp)
                        left +=1
                        right-=1
                    elif nums[left] + nums[right] < x:
                        left += 1
                    else:
                        right -=1
        return result

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums, result, lookup = sorted(nums), [], {}
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)): 
                if nums[i] + nums[j] not in lookup:
                    lookup[nums[i] + nums[j]] = []
                lookup[nums[i] + nums[j]].append([i, j])

        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target -i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)