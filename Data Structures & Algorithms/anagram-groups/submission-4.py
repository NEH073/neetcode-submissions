class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in ana:
                ana[key].append(s)
            else:
                ana[key]=[s]
        return list(ana.values())