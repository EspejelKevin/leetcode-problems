"""

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
 
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "tttle"
Output: false

"""

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    mapping = {}

    for i, ch in enumerate(s):
        if (ch in mapping and mapping[ch] != t[i]) or \
           (ch not in mapping and t[i] in list(mapping.values())): 
            return False
        
        mapping[ch] = t[i]
    
    return True
