"""
12) Check if a tree is a binary search tree.

In BST, the element in the root is:
- Greater than or equal to the numbers on the left
- Less than or equal to the number on the right
- The definition of a tree node: Node(value, left, right)
- Both the left and right subtrees must also be binary search trees.




Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


class TreeNode():
    """Definition for a binary tree node. """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr: list[int], i: int, n: int) -> TreeNode | None:
    """
    Build tree pproach:
    2i + 1 for the left child index
    2i + 2 for the right
    """
    root = None
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_tree(arr, 2 * i + 1, n)
        root.right = build_tree(arr, 2 * i + 2, n)
    return root


def is_valid_bst(root: TreeNode, lower_bound=None, upper_bound=None) -> bool:
    check_node = True
    check_left = True
    check_right = True

    if root is not None:
        if lower_bound:
            check_node = lower_bound < root.val
        if upper_bound:
            check_node = root.val < upper_bound

        check_left = is_valid_bst(root.left, upper_bound=root.val)
        check_right = is_valid_bst(root.left, lower_bound=root.val)

    return check_node and check_left and check_right


def main():
    arr = [2, 1, 3]
    #arr = [5, 1, 4, None, None, 3, 6]
    #arr = [1, 2, 3, None, 4, None, None, 5, 6, None, 7]
    root = build_tree(arr, 0, len(arr))
    result = is_valid_bst(root=root)
    print(result)


main()









