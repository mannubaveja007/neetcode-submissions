class Solution:
    def helper(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if (s[i] in hashmap ) and (hashmap[s[i]] != t[i]):
                return False
            hashmap[s[i]] = t[i]
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s,t) and self.helper(t,s)
