class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j= n-1
        k = m+n-1

        if n==0:
            nums1[0:m] = nums1[0:m]
        elif m==0:
            nums1[0:n] = nums2[0:n]
        else:
            while True:
                if(nums1[i] < nums2[j]):
                    nums1[k] = nums2[j]
                    j-=1
                else:
                    nums1[k]= nums1[i]
                    i-=1
                k-=1

                if(i<0 or j< 0):
                    break
            if(j>=0):
                nums1[0:j]=nums2[0:j]
nums1 = [0]
m = 0
nums2 = [1]
n = 1
s = Solution()
s.merge(nums1,m,nums2,n)
print(nums1)






