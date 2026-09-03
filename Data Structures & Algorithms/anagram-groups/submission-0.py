class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # create dictionary to hold the groups of anagrams

        for word in strs:
            # create signature (alphabetical order)
            signature = ''.join(sorted(word)) # sorted() makes word become a list of chars

            # check to see if signature is already in groups, if not, add it
            if signature not in groups:
                groups[signature] = []
            
            # add that word to it's matching signature group
            groups[signature].append(word)
        
        return list(groups.values())