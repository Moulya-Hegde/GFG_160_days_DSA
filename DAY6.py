'''
Majority Element II
Difficulty: Medium
You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format
'''
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        d={}
        res=[]
        third=len(arr)/3
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]>third:
                res.append(i)
        res.sort()
        return res
        