class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or k <= 0:
            return []
            
        def get_dist(point):
            # Calculate squared distance from origin
            return point[0] * point[0] + point[1] * point[1]
            
        def partition(left, right, pivot_idx):
            pivot_dist = get_dist(points[pivot_idx])
            # Move pivot to end
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            store_idx = left
            
            # Partition points based on distance
            for i in range(left, right):
                if get_dist(points[i]) < pivot_dist:
                    points[i], points[store_idx] = points[store_idx], points[i]
                    store_idx += 1
                    
            # Move pivot to final position
            points[right], points[store_idx] = points[store_idx], points[right]
            return store_idx
            
        def quick_select(left, right, k):
            if left == right:
                return
                
            # Choose random pivot
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)
            
            if pivot_idx == k:
                return
            elif pivot_idx < k:
                quick_select(pivot_idx + 1, right, k)
            else:
                quick_select(left, pivot_idx - 1, k)
                
        n = len(points)
        quick_select(0, n-1, k)
        return points[:k]