class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                                          
        is_balanced = True
        index = 0
        while index < len(s) and is_balanced:
            paren = s[index]
            if paren in '({[':
                stack.append(paren)
            else:
                if not stack:
                    is_balanced = False
                else:
                    top = stack.pop()
                    if not is_match(top, paren):
                        is_balanced = False
            index += 1
            
            def is_match(p1, p2):
                if p1 == '(' and p2 == ')':
                    return True
                elif p1 == '[' and p2 == ']':
                    return True
                elif p1 == '{' and p2 == '}':
                    return True
                else:
                    return False

        if not stack and is_balanced == True:
            return True
        else:
            return False