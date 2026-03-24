def fact(a):
    f=1
    if a == 0 :
        return f
    else:
        for x in range(1,a+1):
            f*=x
        return f

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k=k-1
        s=''
        a=[x for x in range(1,n+1)]
        for x in range(n-1,-1,-1):
            z,k=divmod(k,fact(x))
            s+=str(a.pop(z))
        return s
        