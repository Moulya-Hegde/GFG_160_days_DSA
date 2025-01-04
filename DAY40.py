'''
Count all triplets with given sum in sorted array
Difficulty: Medium
Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Two triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 
Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i], target ≤ 105
'''
class Solution:
    def countTriplets(self, arr, target):
        n=len(arr)
        count=0
        for i in range(n-2):
            j,k=i+1,n-1
            while j<k:
                cur=arr[i]+arr[j]+arr[k]
                if cur==target:
                    left,right=0,0
                    t1,t2=arr[j],arr[k]
                    while j<=k and arr[j]==t1:
                        left+=1
                        j+=1
                    while k>=j and arr[k]==t2:
                        right+=1
                        k-=1
                    if t1==t2:
                        count+=int(left*(left-1)/2)
                    else:
                        count+=left*right
                elif cur<target:
                    j+=1
                else:
                    k-=1
        return count
                    