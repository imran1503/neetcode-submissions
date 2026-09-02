class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap ( Element : times element appears in array)

        #check if a elem's appearances is > 1, if so return elem. 
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

            if counts[num] > 1:
                return True

        return False