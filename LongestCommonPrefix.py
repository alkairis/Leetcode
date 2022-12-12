# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    # @return a string
    
    def matchString(self, string1, string2):
        if(string1==string2):
            return string1
        return self.matchString(string1[0:len(string1)-1], string2[0:len(string2)-1])
        
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_length = min([len(i) for i in strs])
        
        newstr = list(set(i[0:min_length] for i in strs))
        prefix = newstr[0]
        
        for i in range(1, len(newstr)):
            if(prefix==newstr[i]):
                continue
            else:
                prefix = self.matchString(prefix, newstr[i])
                newstr = list(i[0:len(prefix)] for i in newstr)
        return prefix
            
        
s = Solution()
print(s.longestCommonPrefix(["abca","aba","aaab"]))
print(s.longestCommonPrefix(["car","dog","hacar"]))
print(s.longestCommonPrefix(["flower","flow","flip"]))