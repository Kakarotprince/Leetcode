class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l=list()
        for x in range(left,right+1):
            t=x
            f=1
            while t:
                t,r=divmod(t,10)
                if r==0 or x%r!=0:
                    f=0
                    break
            if f:
                l.append(x)
        return l