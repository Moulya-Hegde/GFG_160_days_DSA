'''
Count Subarrays with given XOR
Difficulty: Medium
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.
'''
class Solution:
    def subarrayXor(self, arr, k):
        d={}
        count=0
        xor=0
        for i in arr:
            xor^=i
            if xor ==k:
                count+=1
            pre=xor^k
            if pre in d:
                count+=d[pre]
            if xor in d:
                d[xor]+=1
            else:
                d[xor]=1
        return count