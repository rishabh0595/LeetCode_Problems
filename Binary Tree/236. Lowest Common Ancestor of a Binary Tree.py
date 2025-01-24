"""

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(current_node: TreeNode) -> bool:

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            left = recurse_tree(current_node.left)

            right = recurse_tree(current_node.right)


            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            print(f'mid is {mid}, left is {left} and right is {right}')
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            print(f'return - { mid or left or right}\n')
            return mid or left or right

        recurse_tree(root)
        return self.ans
        
# class Solution:

#     def __init__(self):
#         self.ans = None

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         def dfs(node):
#             if not node:
#                 return False
            
#             left = dfs(node.left)
#             right = dfs(node.right)

#             equal = (node == p) or (node == q)

#             if equal+left+right >=2:
#                 self.ans = node

#             return equal or left or right

    
#         dfs(root)
#         return self.ans