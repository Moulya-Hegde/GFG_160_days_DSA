'''
Sum Pair closest to target
Difficulty: Easy
Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.
'''
class Solution:
    def sumClosest(self, arr, target):
        if len(arr)<2:
            return []
        arr.sort()
        res=[]
        diff=float('inf')
        n=len(arr)
        i,j=0,n-1
        while i<j:
            cur_sum=arr[i]+arr[j]
            if cur_sum==target:
                return [arr[i],arr[j]]
            elif cur_sum<target:
                cur_diff=abs(target-(arr[i]+arr[j]))
                if cur_diff<diff:
                    diff=cur_diff
                    res=[arr[i],arr[j]]
                i+=1
            else:
                cur_diff=abs(target-(arr[i]+arr[j]))
                if cur_diff<diff:
                    diff=cur_diff
                    res=[arr[i],arr[j]]
                j-=1
        return res