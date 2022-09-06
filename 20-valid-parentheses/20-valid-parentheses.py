class Solution:
    def isValid(self, s: str) -> bool:
        leng = len(s)
        stack = []
        stack.append(s[0])
        
        for i in range(1, leng):
          if len(stack) == 0:
            stack.append(s[i])
          elif (stack[-1] == '(' and s[i] == ')'):
            stack.pop()
          elif (stack[-1] == '{' and s[i] == '}'):
            stack.pop()
          elif (stack[-1] == '[' and s[i] == ']'):
            stack.pop()
          else:
            stack.append(s[i])
        
        return len(stack) == 0
            