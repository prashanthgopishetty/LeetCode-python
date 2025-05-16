class Solution:
    def maxArea(self, height):
        left = 0;
        right = len(height)-1
        max_area = 0
        while(right > left):
            temp_area = min(height[left], height[right]) *(right-left)
            max_area = max(max_area, temp_area)
            if(arr[right] > arr[left]):
                left+=1
            else:
                right-=1

        return max_area

s = Solution()
arr = [2,3,4,5,18,17,6]
print(s.maxArea(arr))