class Solution:
    def kClosest(self, points, k: int):
        # Calculates distance
        dist = [point[0]**2 + point[1]**2 for point in points]

        # Finds kth smallest distance using quick select
        def partition(arr, left, right):
            pivot = arr[right]
            i = left
            for j in range(left, right):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[right] = arr[right], arr[i]
            return i

        def quick_select(arr, k, left, right):
            pivot_ind = partition(arr, left, right)
            # Found kth smallest
            if pivot_ind == k - 1:
                return arr[pivot_ind]
            # Recur to smaller array
            elif pivot_ind < k - 1:
                return quick_select(arr, k, pivot_ind + 1, right)
            # Recur to bigger array
            else:
                return quick_select(arr, k, left, pivot_ind - 1)

        kth_smallest = quick_select(dist, k, 0, len(dist) - 1)
  
        # Return output
        output = []
        for point in points:
            if point[0]**2 + point[1]**2 <= kth_smallest:
                output.append(point)
        return output

solution = Solution()
ans = solution.kClosest([[1,3],[-2,2]], 1); assert ans == [[-2,2]], ans
ans = solution.kClosest([[3,3],[5,-1],[-2,4]], 2); assert ans == [[3,3],[-2,4]], ans
ans = solution.kClosest([[1,3],[-2,2],[2,-2]], 2); assert ans == [[-2,2],[2,-2]], ans
ans = solution.kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3); assert ans == [[0,2],[-3,3],[-2,5]], ans
