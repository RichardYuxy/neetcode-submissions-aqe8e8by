class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights)+1):
            while stack and (i == len(heights) or heights[stack[-1]]>heights[i]):
                height = heights[stack.pop()]
                maxArea = max(maxArea, i*height if not stack else height * (i-1-stack[-1]))

            stack.append(i)

        return maxArea