class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if root is None:
        #     return 0

        
        def dfs(root1,root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False

            if root1.val != root2.val:
                return False
            

            return dfs(root1.left,root2.left) and dfs(root1.right,root2.right)


        return dfs(p,q)

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false

"""