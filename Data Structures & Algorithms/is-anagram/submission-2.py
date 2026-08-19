class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If able to use libraries use Counter which counts frequency of elements in a string
        # return Counter(s) == Counter(t)
        
        if len(s) != len(t):
            return False

        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1        
        for ch in t:
            counts[ch] = counts.get(ch, 0) - 1

        for count in counts.values():
            if(count != 0):
                return False

        return True        
        
