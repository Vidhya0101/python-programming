# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def fun(x):
            if x.left:
                fun(x.left)
            if x:
                r.append(x.val)
            if x.right:
                fun(x.right)
        fun(root)
        c=Counter(r)
        # Mode means the element which has the highest frequency in the array(बहुलक)
        mxval=max(c.values())
        return [i for i in c if c[i]==mxval]

       
        


      
