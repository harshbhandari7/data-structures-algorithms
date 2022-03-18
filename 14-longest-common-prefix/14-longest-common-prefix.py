class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_s, max_s = min(strs), max(strs)
        i = 0
        while(i < len(min_s)):
            if min_s[i] != max_s[i]:
                min_s = min_s[:i]
            i += 1
        return min_s