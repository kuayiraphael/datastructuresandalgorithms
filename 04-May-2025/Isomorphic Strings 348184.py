# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If the strings are of different lengths, they cannot be isomorphic.
        if len(s) != len(t):
            return False

        mapping_s_to_t = {}
        mapping_t_to_s = {}

        # Iterate over both strings at the same time.
        for char_s, char_t in zip(s, t):
            # If there's already a mapping for char_s, check if it's consistent with char_t.
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                mapping_s_to_t[char_s] = char_t

            # Similarly, check that char_t maps back to char_s.
            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s

        return True
