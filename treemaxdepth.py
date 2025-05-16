class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_depth(root):
    # If the tree is empty, the depth is 0
    if root is None:
        return 0

    # Recursively get the depth of the left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # The maximum depth of the tree is the greater of the two depths, plus 1 for the current node
    return max(left_depth, right_depth) + 1

# Example binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

print("Maximum Depth of the Tree:", max_depth(root))  # Output: 3
