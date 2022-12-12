# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)<2) or len(s)%2!=0:
            return False
        brackets = {"{":"}","[":"]","(":")"}
        
        finalList = []
        for i in s:
            if(i in brackets):
                finalList.append(brackets.get(i))
            elif i not in finalList[-1]:
                finalList.pop()
            else:
                return False
        return bool(finalList)

sol = Solution()
print(sol.isValid("()[]{}"))