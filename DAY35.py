'''
Union of Arrays with Duplicates
Difficulty: Easy
Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct.
'''

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        set1=set(a)
        set2=set(b)
        return len(set1.union(set2))