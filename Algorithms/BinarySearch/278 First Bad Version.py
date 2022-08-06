# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        begin =0
        end = n
        p = 0
        while begin<=end:
            mid =(end + begin)//2 
            if isBadVersion(mid) == True:
                end = mid-1
                p= mid
            else:
                begin = mid +1
        return p
                