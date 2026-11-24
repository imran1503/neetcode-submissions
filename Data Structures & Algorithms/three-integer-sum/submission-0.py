class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()           
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early exit: smallest anchor already > 0 → no triplet possible
            if nums[i] > 0:
                break
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1             # need bigger sum
                elif total > 0:
                    right -= 1            # need smaller sum
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
