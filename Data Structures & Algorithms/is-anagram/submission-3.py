class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         s_hm = {}
         t_hm = {}

         if len(s) != len(t):
            return False

         for letter in s:
            if letter in s_hm.keys():
                s_hm[letter] += 1
            else:
                s_hm[letter] = 1

         for letter in t:
            if letter in t_hm.keys():
                t_hm[letter] += 1
            else:
                t_hm[letter] = 1
        
         return s_hm == t_hm

            

