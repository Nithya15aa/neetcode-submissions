class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram, t_a = {},{}
        for ch in s:
            anagram[ch] = anagram.get(ch,0) + 1
        for ch in t:
            t_a[ch] = t_a.get(ch,0) + 1
        return anagram == t_a
        


        