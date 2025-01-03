'''
Move All Zeroes to End
Difficulty: Easy
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
'''
class Solution:
    def pushZerosToEnd(self,arr):
        k=-1
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[k+1]=arr[i]
                k+=1
                k+=1
        while k<len(arr):
            arr[k]=0
            k+=1