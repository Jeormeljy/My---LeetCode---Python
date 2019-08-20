'''

205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 

No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Example 2:

Input: s = "foo", t = "bar"

Output: false

Example 3:

Input: s = "paper", t = "title"

Output: true

Note:

You may assume both s and t have the same length.

'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None and t is None:
            return True
        elif s is None or t is None or len(s) != len(t):
            return False
        dct1 = {}
        dct2 = {}
        for i in range(len(s)):
            if s[i] not in dct1 and t[i] not in dct2:
                dct1[s[i]] = t[i]
                dct2[t[i]] = s[i]
            elif s[i] not in dct1 or t[i] not in dct2 or dct1[s[i]] != t[i] or dct2[t[i]] != s[i]:
                return False
        return True
