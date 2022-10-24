class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        closestPoints = []
        
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
            
        heapq.heapify(minHeap)                  # Create a heap from a list in O(n) time
        
        while k > 0:
            dist, x, y = heapq.heappop(minHeap) # Pop and return the smallest item from the heap
            closestPoints.append([x, y])        
            k -= 1
            
        return closestPoints