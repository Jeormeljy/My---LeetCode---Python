'''

266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"

Output: false

Example 2:

Input: "aab"

Output: true

Example 3:

Input: "carerac"

Output: true

'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) <= 1:
            return True
        visited = {}
        odd = 0
        for i in xrange(len(s)):
            if s[i] not in visited:
                visited[s[i]] = 1
                odd += 1
            else:
                visited[s[i]] += 1
                if visited[s[i]] % 2 == 1:
                    odd += 1
                else:
                    odd -= 1
        return odd <= 1
