class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_leng = len(strs)
        smallest = strs[0]
        for i in range(1, strs_leng):
            if (len(strs[i]) < len(smallest)):
                smallest = strs[i]
        common_prefix = smallest
        itr = len(common_prefix)
        while (itr > -1):
            for i in range(strs_leng):
                if (strs[i].startswith(common_prefix)):
                    itr -= 1
                    continue
                else:
                    common_prefix = common_prefix[:-1]
                    itr = len(common_prefix)
                    break
        return common_prefix