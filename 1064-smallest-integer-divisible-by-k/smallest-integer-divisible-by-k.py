class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        s=0;count=0
        if k%2==0 or k%5==0:
            return -1
        while 1:
            count+=1
            s=(s*10+1)%k
            if s==0:
                return count
            