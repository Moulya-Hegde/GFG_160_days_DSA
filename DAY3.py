'''
Reverse an Array
Difficulty: Easy
You are given an array of integers arr[]. Your task is to reverse the given array.
'''
class Solution:
    def reverseArray(self, arr):
        i=0
        j=len(arr)-1
        while i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1