class Solution:
    def romanToInt(self, s: str) -> int:
        result, i = 0, 0
        romans = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        while(i<len(s)):
            s1 = romans.get(s[i])
            if(i+1 < len(s)):
                s2 = romans.get(s[i+1])
                print(s1, s2)
                if(s1>=s2):
                    result+=s1
                    i+=1
                else:
                    result+= s2-s1
                    i+=2
            else:
                result+=s1
                i+=1
            
        return result
        
s = Solution().romanToInt("MCDLXXVI")
print(s)
