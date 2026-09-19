class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # Find the nearest point on the rectangle to the circle's center
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        
        # Calculate the distance components
        dx = xCenter - nearest_x
        dy = yCenter - nearest_y
        
        # Check if squared distance is within the squared radius
        return (dx * dx + dy * dy) <= (radius * radius)