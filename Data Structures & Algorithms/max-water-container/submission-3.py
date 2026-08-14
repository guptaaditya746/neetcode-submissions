class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # Create pairs of (height, original_index) and sort descending by height
        indexed_heights = [(h, i) for i, h in enumerate(heights)]
        indexed_heights.sort(reverse=True, key=lambda x: x[0])
        
        max_area = 0
        
        # Track the leftmost and rightmost indices of the lines we've processed so far
        # Initialize them with the index of the tallest line
        min_seen_idx = indexed_heights[0][1]
        max_seen_idx = indexed_heights[0][1]
        
        for h, i in indexed_heights:
            # h is guaranteed to be the limiting height for any previously seen line.
            # Calculate the area using the furthest left and furthest right taller lines.
            area_left = h * abs(i - min_seen_idx)
            area_right = h * abs(i - max_seen_idx)
            
            # Update max_area
            if area_left > max_area: max_area = area_left
            if area_right > max_area: max_area = area_right
            
            # Expand our window of seen indices
            if i < min_seen_idx: min_seen_idx = i
            if i > max_seen_idx: max_seen_idx = i
            
        return max_area