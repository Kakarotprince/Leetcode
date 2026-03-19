class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        diff=arr[0]-arr[1]
        for x in range(1,len(arr)):
            if diff != arr[x-1] - arr[x]:
                return False
        return True
        