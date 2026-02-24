class Solution:
    def kClosest(self, points, k):
        # сортируем точки по квадрату расстояния до (0,0)
        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        return points[:k]