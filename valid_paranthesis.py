
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""


def isValid(s: str) -> bool:
    
    
    stack = []
    
    paranthesis_map = {")":"(", "}":"{", "]":"["}
    
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack and stack.pop() != paranthesis_map[ch]:
                return False
    
    return True if not stack else False
                
