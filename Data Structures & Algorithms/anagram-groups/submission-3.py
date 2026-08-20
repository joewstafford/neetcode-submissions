class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for str in strs:
            sort = "".join(sorted(str))
            my_dict.setdefault(sort, []).append(str)
        return list(my_dict.values())
                
        




