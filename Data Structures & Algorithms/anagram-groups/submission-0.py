class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict=defaultdict(list)
        for element in strs:
            sortedChars= ''.join(sorted(element))
            resultDict[sortedChars].append(element)
        return list (resultDict.values())
