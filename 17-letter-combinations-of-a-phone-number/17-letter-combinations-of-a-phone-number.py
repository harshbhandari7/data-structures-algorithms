class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ddict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                 '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
            oldlist = []
        else:
            oldlist = ['']
            for d in digits:
                newlist = []
                for ss in ddict[d]:
                    newlist.extend([s + ss for s in oldlist])
                oldlist = newlist
        return oldlist