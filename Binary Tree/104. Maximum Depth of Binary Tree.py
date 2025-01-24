
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            return 1 + max(left,right)

        return dfs(root)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [(1,root),]
        maxDepth = 1
        currDepth = 1
        while stack:
            currDepth , root = stack.pop()
            maxDepth = max(currDepth,maxDepth)

            if root.left:
                stack.append((1+currDepth,root.left))
            
            if root.right:
                stack.append((1+currDepth,root.right))
            
        return maxDepth


"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""