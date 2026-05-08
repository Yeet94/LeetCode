# Last updated: 5/8/2026, 4:23:15 PM
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
       
        queue = deque([(p,q)])


        while queue:
            pair = queue.popleft()
            p_node = pair[0]
            q_node = pair[1]


            if not p_node and not q_node:
                continue
           
            if not p_node or not q_node:
                return False


            if p_node.val!= q_node.val:
                return False


            queue.append((p_node.left, q_node.left))
            queue.append((p_node.right, q_node.right))


        return True