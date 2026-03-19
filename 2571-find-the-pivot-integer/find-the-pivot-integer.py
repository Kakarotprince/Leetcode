class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=sum([x for x in range(n+1)])
        f=0
        for x in range(1,n+1):
            if x+f==s:
                return x
            f+=x;s-=x
        return -1
        