class Solution:
    def kClosest(self, points, k: int):
        # Calculates distance
        dist = [(point, point[0]**2 + point[1]**2) for point in points]

        # Finds kth smallest distance using quick select





        kth_smallest = sorted(dist, key=lambda x: x[1])[k-1][1]
        
        # Return output
        output = []
        for p, d in dist:
            if d <= kth_smallest:
                output.append(p)
        return output

solution = Solution()
ans = solution.kClosest([[1,3],[-2,2]], 1); assert ans == [[-2,2]], ans
ans = solution.kClosest([[3,3],[5,-1],[-2,4]], 2); assert ans == [[3,3],[-2,4]], ans
