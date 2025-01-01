'''
Print Anagrams Together

Difficulty: Medium

Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Note: The final output will be in lexicographic order.
'''
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        d = {}
        for i in arr:
            key = "".join(sorted(i))  # Sort the string to create the key
            if key not in d:
                d[key] = []  # Initialize an empty list if key is not present
            d[key].append(i)  # Append the word to its group
        
        res = []
        for k in d:
            res.append(d[k])  # Collect all groups of anagrams
        
        return res
        