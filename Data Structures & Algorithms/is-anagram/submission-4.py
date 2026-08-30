class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_freq = {}
        t_char_freq = {}

        for char in s:
            if char in s_char_freq:
                s_char_freq[char] += 1
            else:
                s_char_freq[char] = 1
        
        for char in t:
            if char in t_char_freq:
                t_char_freq[char] += 1
            else:
                t_char_freq[char] = 1
        
        return s_char_freq == t_char_freq

        