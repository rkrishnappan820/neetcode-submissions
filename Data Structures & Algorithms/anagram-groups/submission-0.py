class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for word in strs:
            alpha_word = "".join(sorted(word))
            my_dict[alpha_word].append(word)
        return list(my_dict.values())