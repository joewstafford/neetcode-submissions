class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - 97] += 1   # ord('a') == 97, hardcoded to skip a function call
            groups[tuple(count)].append(s)

        return list(groups.values())