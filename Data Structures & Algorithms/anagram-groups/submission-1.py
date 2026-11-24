class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        groups = {}
        counter = 0

        for string in strs:
            key = tuple(sorted(string))
            if key in groups:
                output[groups[key]].append(string)
            else:
                groups[key] = counter
                output.append([string])
                counter += 1

        return output