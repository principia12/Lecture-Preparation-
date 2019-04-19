"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            if root.children:
                result = []
                for subtree in root.children:
                    result += Solution.postorder(Solution, subtree)
                result.append(root.val)
                return result
            else:
                return [root.val]
        else:
            return []