"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

"""

def is_nnagram(s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))