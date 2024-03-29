class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        leng1 = len(v1)
        leng2 = len(v2)
        
        if leng1 < leng2:
          diff = leng2 - leng1
          for i in range(diff):
            v1.append('0')
        elif leng1 > leng2:
          diff = leng1 - leng2
          for i in range(diff):
            v2.append('0')
            
        for i in range(len(v1)):
          if int(v1[i]) > int(v2[i]):
            return 1
          elif(int(v1[i]) < int(v2[i])):
            return -1
        
        return 0