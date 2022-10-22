# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root                                      
        
        while ans:
            if p.val > ans.val and q.val > ans.val:     # If both p and q are greater than parent
                ans = ans.right
            elif p.val < ans.val and q.val < ans.val:   # If both p and q are lesser than parent
                ans = ans.left
            else:
                return ans
        
        return