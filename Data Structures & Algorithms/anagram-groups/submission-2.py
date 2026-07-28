from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = defaultdict(list)
        result= []
        for s in strs:
            sorted_s = tuple(sorted(s))

            a_map[sorted_s].append(s)

        return list(a_map.values())