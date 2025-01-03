'''
Second Largest
Difficulty: Easy
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
'''
class Solution:
    def getSecondLargest(self, arr):
        lar1=arr[0]
        lar2=0
        for i in arr:
            if i>lar1:
                lar2=lar1
                lar1=i
            elif i<lar1 and i>lar2:
                lar2=i
        if lar2==0:
            return -1
        return lar2
