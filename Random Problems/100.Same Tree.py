"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
1.
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        	if(not p and not q):
            return True
        elif(not p and q):
            return False
        elif(p and not q):
            return False
        elif(p.val != q.val):
            return False
        else:
            return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)

"""
2.
"""
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # advance both trees together with iterative DFS
        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node and q_node:
				# if nodes have same value, keep traversing
                if p_node.val == q_node.val:
                    stack.append((p_node.right, q_node.right))
                    stack.append((p_node.left, q_node.left))
				# if nodes have different value, early return
                else:
                    return False
			# if only one node is null, early return
            elif p_node or q_node:
                return False
		# DFS traversal finished successfuly, trees are equal
        return True
        """