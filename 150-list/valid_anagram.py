class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s, dict_t = {}, {}
        for a,b in zip(s,t):
            dict_s[a] = dict_s.get(a,0) + 1
            dict_t[b] = dict_t.get(b,0) + 1
        return dict_s == dict_t