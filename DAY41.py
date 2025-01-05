'''
Count Pairs whose sum is less than target
Difficulty: Easy
Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.
'''
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        arr.sort()
        n=len(arr)
        count=0
        if n<2:
            return 0
        left,right=0,n-1
        while left<right:
            if arr[left]+arr[right]<target:
                count+=(right-left)
                left+=1
            else:
                right-=1
        return count