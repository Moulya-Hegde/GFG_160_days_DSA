'''
Question: 

Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero. 
Returned triplet should also be internally sorted i.e. i<j<k.

Difficulty:Medium

Intuition:
Sort array so that it is easy to use 2 pointer.
** num1+num2 = -num3
this leads to zero sum
with every element traverse array till end to find all combinations.
Avoid duplicates by moving past them


Time complexity: O(n^2)

'''
class Solution:
    def findTriplets(self, arr):
        arr.sort() #Sorting O(nlogn)
        n=len(arr)
        triplets=[]
        for i in range(n-2):
            if i>0 and arr[i]==arr[i-1]: #skip duplicate check for first element
                continue
            target=-arr[i] #negate
            left,right=i+1,n-1
            while left < right:
                cur=arr[left]+arr[right]
                if cur==target:
                    triplets.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:
                        right-=1
                elif cur<target: #implies cur value needs an increase. sorted array->smaller values on left and greater on right.
                    left+=1
                else: #implies decrease
                    right-=1
        return triplets
