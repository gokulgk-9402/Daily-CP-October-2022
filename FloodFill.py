class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            old = image[sr][sc]
            rows = len(image)
            cols = len(image[0])
            image[sr][sc] = color

            for i,j in zip((sr, sr+1, sr, sr-1),(sc+1,sc,sc-1, sc)):
                if i >= 0 and i<rows and j>=0 and j<cols and image[i][j] == old:
                    self.floodFill(image,i,j,color)

        return image