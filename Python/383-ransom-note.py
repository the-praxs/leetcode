class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        mag_dict = Counter(magazine)
        
        for char in ransom_dict.keys():
            # If the character is not in the magazine 
            # or its count is more than present in magazine, 
            # return False
            if char not in mag_dict.keys() or ransom_dict[char] > mag_dict[char]:
                return False
        
        return True