class Solution:
    def dfs(self, image: List[List[int]], sr: int, sc: int, source: int, color: int) -> List[List[int]]:
        # If the current pixel is out of the image, return
        # If the currrnt pixel is not the source color, return
        if (sr < 0) or (sc < 0) or (sr >= len(image)) or (sc >= len(image[0])) or (image[sr][sc] != source):
            return
        
        image[sr][sc] = color                       # Set the current pixel to the new color
        
        self.dfs(image, sr-1, sc, source, color)    # Check the pixel above
        self.dfs(image, sr+1, sc, source, color)    # Check the pixel below
        self.dfs(image, sr, sc-1, source, color)    # Check the pixel to the left
        self.dfs(image, sr, sc+1, source, color)    # Check the pixel to the right
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        self.dfs(image, sr, sc, image[sr][sc], color)   # Call the DFS function
        
        return image


# Another solution
# class Solution(object):
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if(image[sr][sc]==color):
#             return image

#         temp=image[sr][sc]
#         stack=[(sr,sc)]

#         while stack:
#             i,j=stack.pop()

#             if (image[i][j]==temp):
#                 image[i][j]=color
#                 if(i+1<len(image)):
#                     stack.append((i+1,j))

#                 if i >= 1:
#                     stack.append((i-1,j))

#                 if(j+1<len(image[0])):
#                     stack.append((i,j+1))

#                 if j >= 1:
#                     stack.append((i,j-1))
                    
#         return image