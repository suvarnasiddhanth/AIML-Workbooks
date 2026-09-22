class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def search(self, val, node=None):
        if node is None:
            node = self.root

        if node is None or node.value == val:
            return node

        if val < node.value and node.left:
            return self.search(val, node.left)
        elif val > node.value and node.right:
            return self.search(val, node.right)

        return None

    def traverse_for_insert(self, val, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None

        if val < node.value:
            if node.left is not None:
                return self.traverse_for_insert(val, node.left)
            return node
        elif val > node.value:
            if node.right is not None:
                return self.traverse_for_insert(val, node.right)
            return node
        return node

    def insert(self, val):
        new_node = Node(val)

        # Case 1: Empty tree
        if self.root is None:
            self.root = new_node
            return

        parent_node = self.traverse_for_insert(val)

        # Ignore duplicate values
        if parent_node.value == val:
            return

        new_node.parent = parent_node
        if val < parent_node.value:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

    def _min_value_node(self, node):
        """Helper to find the node with the smallest value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, val):
        node = self.search(val)
        if node is None:
            return False  # Value not found

        # Case 1: Node has no children (Leaf node)
        if node.left is None and node.right is None:
            self._replace_node_in_parent(node, None)

        # Case 2: Node has only one child
        elif node.left is None:
            self._replace_node_in_parent(node, node.right)
        elif node.right is None:
            self._replace_node_in_parent(node, node.left)

        # Case 3: Node has two children
        else:
            # Find the in-order successor (smallest node in the right subtree)
            successor = self._min_value_node(node.right)
            node.value = successor.value
            # Recursively delete the successor
            self._delete_node(successor)

        return True

    def _delete_node(self, node):
        """Internal helper for deleting a node with 0 or 1 child."""
        child = node.left if node.left is not None else node.right
        self._replace_node_in_parent(node, child)

    def _replace_node_in_parent(self, node, new_child):
        """Updates parent pointers when replacing a node."""
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = new_child
            else:
                node.parent.right = new_child
        else:
            self.root = new_child

        if new_child is not None:
            new_child.parent = node.parent