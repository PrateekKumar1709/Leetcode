class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range (len(heights) +1):
            current_heights = heights[i] if i < len(heights) else 0

            while stack and current_heights < heights[stack[-1]]:
                height = heights[stack.pop()]

                width = i - stack[-1] - 1 if stack else i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area