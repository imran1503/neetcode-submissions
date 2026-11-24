from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hm = {}
        for num in nums:
            hm[num] = True

        longest = 0

        for num in nums:
            # Only start counting if num is the beginning of a sequence
            if (num - 1) in hm:
                continue
            length = 1
            current = num + 1
            while current in hm:
                length += 1
                current += 1
            longest = max(longest, length)
        return longest