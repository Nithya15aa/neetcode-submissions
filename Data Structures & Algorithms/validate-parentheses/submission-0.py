class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_to_close = {
            ")" : "(",
            "}" :  "{",
            "]" :  "["
        }

        for ch in s:
            
            if ch not in open_to_close:
                stack.append(ch)
            else:
                if not stack or stack[-1] != open_to_close[ch]:
                    return False
                stack.pop()  
        return not stack

            
            

        
        