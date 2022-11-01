class Solution:
    def isValid(self, s: str) -> bool:
        vals = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        for x in s:
            if x in vals:
                if stack and stack[-1] == vals[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        if not stack:
            return True
        return False

if __name__ == '__main__':
    inp = "()[]{}"
    print(Solution().isValid(inp))
            
            

        
        



            

        