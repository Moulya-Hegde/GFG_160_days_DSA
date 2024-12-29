'''
Intersection of Two arrays with Duplicate Elements

Difficulty:Easy

Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not have duplicate elements and the result should contain items in any order.

Note: The driver code will sort the resulting array in increasing order before printing.

Intuition: 
Intersection part of set operations
'''

class Solution:
    def intersectionWithDuplicates(self, a, b):
        seta=set(a)
        setb=set(b)
        return list(seta.intersection(setb))