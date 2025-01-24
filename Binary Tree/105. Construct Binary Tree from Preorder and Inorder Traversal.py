
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        
        rootVal = (preorder[0])
        index = inorder.index(rootVal)

        root = TreeNode(rootVal)

        left = self.buildTree(preorder[1:index+1],inorder[:index])
        right = self.buildTree(preorder[index+1:],inorder[index+1:])


        root.left = left
        root.right = right

        return root




"""

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

"""