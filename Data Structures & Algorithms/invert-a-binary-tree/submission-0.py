# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)

        if root is None:
            return None
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root 





        #DFS
        # if not root:
        #     return None
        
        # # swap
        # root.left, root.right = root.right, root.left
        
        # # recurse
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        
        # return root