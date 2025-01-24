
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder or not postorder:
            return None
        

        rootval = postorder.pop()
        index = inorder.index(rootval)
        root = TreeNode(rootval)

        right = self.buildTree(inorder[index+1:],postorder)
        left = self.buildTree(inorder[:index],postorder)
        

        root.left = left
        root.right = right

        return root


"""
Given two integer arrays inorder and postorder where inorder is the i
norder traversal of a binary tree and postorder is the postorder traversal of the same tree, 
construct and return the binary tree.

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 
"""