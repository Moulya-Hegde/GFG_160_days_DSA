'''
Subarrays with sum K
Difficulty: Medium
Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.
'''
class Solution:
    def countSubarrays(self, arr, k):
        d={0:1}
        count=0
        cur=0
        for i in arr:
            cur+=i
            if (cur-k) in d:
                count+=d[cur-k]
            if cur in d:
                d[cur]+=1
            else:
                d[cur]=1
        return count