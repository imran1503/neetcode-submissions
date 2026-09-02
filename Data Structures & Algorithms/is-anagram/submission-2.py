class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts_s = {}
        counts_t = {}
        #load frequency maps
        for char in s:
            counts_s[char] = counts_s.get(char, 0) + 1
        for char in t:
            counts_t[char]= counts_t.get(char, 0) + 1
        #Fail Conditions
        if counts_s.keys() != counts_t.keys(): #Different Letters
            return False
        for k in counts_s.keys():
            if counts_s[k] != counts_t[k]:     #Different letter count in a word
                return False
        return True