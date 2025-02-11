#Time complexity O(n) and space complexity O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#Initializing stack and previous element
        stack=[]
        prev= None
        if not root:
            return True
#Traversing until stack is empty and applying inorder tarversal
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if prev and prev.val>=root.val:
                return False
            prev=root
            root=root.right
            
        return True
