class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        # print(s)
        if not s:
            return 0
        word = s.split()
        return len(word[-1])
