'''
Rotate Array
Difficulty: Medium
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.
'''
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        d=d%len(arr)
        arr[:d]=reversed(arr[:d])
        arr[d:]=reversed(arr[d:])
        arr.reverse()
        