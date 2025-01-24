class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True


        def dfs(root1,root2):

            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False
            
            if root1.val != root2.val:
                return False
            

            return dfs(root1.left,root2.right) and dfs(root1.right,root2.left)


        return dfs(root.left,root.right)

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 



"""