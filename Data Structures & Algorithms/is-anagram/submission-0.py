class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            # Counting appearances of characters in s
            if s[i] not in s_count:
                s_count[s[i]] = 0
            else:
                s_count[s[i]] += 1
            
            # Counting appearances of characters in t
            if t[i] not in t_count:
                t_count[t[i]] = 0
            else:
                t_count[t[i]] += 1
        
        if s_count == t_count:
            return True
        
        return False

            