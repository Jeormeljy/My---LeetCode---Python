'''

49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],

Output:

[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

All inputs will be in lowercase.

The order of your output does not matter.

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs) == 0:
            return []
        dct = {}
        for word in strs:
            dctLst = [0] * 26
            for index in range(len(word)):
                dctLst[ord(word[index]) - ord('a')] += 1
            temp = []
            for num in dctLst:
                temp.append(str(num))
                temp.append('#')
            tempStr = ''.join(temp)
            if tempStr not in dct:
                dct[tempStr] = []
            dct[tempStr].append(word)
        return dct.values()
