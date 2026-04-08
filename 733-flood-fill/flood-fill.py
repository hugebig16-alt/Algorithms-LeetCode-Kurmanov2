class Solution:
    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])
        start = image[sr][sc]

        # ВАЖНО: защита от бесконечной рекурсии
        if start == color:
            return image

        def dfs(r, c):
            # выход за границы
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            # не тот цвет — стоп
            if image[r][c] != start:
                return
            
            # красим
            image[r][c] = color

            # 4 направления
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image