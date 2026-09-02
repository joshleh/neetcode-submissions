class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0 # initialize result
        # initialize dictionary in order to grab values from each symbol
        values = {'I':1 , 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # loop through all the symbols in the roman numeral (except the last one)
        for i in range(len(s)-1):
            if values[s[i]] < values[s[i+1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]
        
        # grab the value from the last symbol and add it to the result
        result += values[s[-1]]
        
        return result