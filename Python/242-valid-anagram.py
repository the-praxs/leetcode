class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                    # if length of s and t are not equal, return False
            return False                    

        s_count, t_count = {}, {}

        for char in s:
            if char not in s_count:
                s_count[char]=1
            else:
                s_count[char]+=1

        for char in t:
            if char not in t_count:
                t_count[char]=1
            else:
                t_count[char]+=1

        if s_count.keys() != t_count.keys():
            return False

        return all(value == t_count[char] for char, value in s_count.items())