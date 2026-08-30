class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for element in strs:
            arr = [0] * 26
            for char in element:
                arr[ord(char) - ord("a")] +=1
            my_dict[tuple(arr)].append(element)
        return list(my_dict.values())
        