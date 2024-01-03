from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_groups[sorted_s].append(s)

        result = list(anagram_groups.values())
        return result
