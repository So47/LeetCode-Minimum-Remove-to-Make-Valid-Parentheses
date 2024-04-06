class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
       stack = []
       output = list(s)

       for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    output[i] = ''

       # Remove unmatched open parentheses
       for index in stack:
           output[index] = ''

       return ''.join(output)
