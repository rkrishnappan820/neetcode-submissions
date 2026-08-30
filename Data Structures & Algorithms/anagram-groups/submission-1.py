class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occur_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            occur_dict[sorted_word].append(word)
        return list(occur_dict.values())