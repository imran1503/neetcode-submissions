class Solution:
    def encode(self, strs: List[str]) -> str:
        returnStr = ''
        for word in strs:
            returnStr += '&&' + word
        return returnStr

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        # split by '&&', ignore the first empty string
        return s.split('&&')[1:]