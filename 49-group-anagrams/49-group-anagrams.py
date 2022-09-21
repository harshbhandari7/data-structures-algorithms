class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        leng = len(strs)
        if leng == 1:
          return [[""]] if strs[0] == "" else [strs[0]]
        
        hash_set = {}
        for s in strs:
          key = ''.join(sorted(s))
          if key in hash_set:
            hash_set[key].append(s)
          else:
            hash_set[key] = [s]
        
        res = []
        for key in hash_set:
          res.append(hash_set[key])
        
        return res
          
        
            