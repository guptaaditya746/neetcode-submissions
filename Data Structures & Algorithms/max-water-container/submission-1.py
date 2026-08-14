class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        n = len(heights)
        j = n-1
        max_area = 0


        while i<j:
            area = (j-i) * min(heights[i],heights[j])


            if heights[i] < heights[j]:
                i += 1
            else :
                j -= 1

            if area > max_area:
                max_area = area

        return max_area