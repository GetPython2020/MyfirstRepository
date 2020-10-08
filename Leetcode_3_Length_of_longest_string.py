    def lengthOfLongestSubstring(s):
        last_appear = {}
        start=0
        longest=0
        
        for index,letter in enumerate(s):
            if letter in last_appear and last_appear[letter] >=start:
                start = last_appear[letter]+1
            else:
                longest = max(longest, index-start+1)
            last_appear[letter]=index
        return longest
