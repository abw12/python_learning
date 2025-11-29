from Node import Node


class BST:
    def __init__(self):
        self.root=None
        self.pre=None
        self.isValid=True


    def insert(self,value):
        # for first node insertion
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if current.value > value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current=current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                current=current.right

    def look_up(self, value):
        if self._look_up_recursive(self.root, value) is False:
            print(f"Not Found: {value}")

    def _look_up_recursive(self, node, value) -> bool:
        if node is None:
            return False

        if node.value == value:
            print(f"Found {node.value}")
            return True
        elif value < node.value:
            return self._look_up_recursive(node.left, value)
        else:
            return self._look_up_recursive(node.right, value)

    def delete(self,value):
        self.root=self._delete_node(self.root,value)

    def _delete_node(self,node,value):
        # Base case node not found
        if not node:
            return None

        if value < node.value:
            node.left=self._delete_node(node.left,value)
        elif value > node.value:
            node.right=self._delete_node(node.right,value)
        else:
            # case 1 : node has no children(leaf node)
            if not node.left and not node.right:
                return None

            # case 2: Node has one child
            if not node.left:
                return node.right # replace with right child
            elif not node.right:
                return node.left # replace with left child

            # case 3: Node has two children
            successor = self._find_min(node.right) # find inorder successor
            node.value = successor.value # copy successor value
            node.right = self._delete_node(node.right,successor.value) # delete successor from its original position
        return node # return modified tree

    def _find_min(self,node):
        """Finds the smallest node in a subtree (leftmost node)"""
        while node.left:
            node=node.left
        return node

    def print_tree(self,node=None,prefix = "Root: "):
        if node is None:
            node=self.root
        if node:
            print(prefix + str(node.value))
            if node.left:
                self.print_tree(node.left,prefix="Left -> ")
            if node.right:
                self.print_tree(node.right,prefix="Right -> ")

    # using the iterative approach for BFS
    def bfs_traversal(self):
        queue=[self.root]
        traversed_nodes=[]
        while queue:
            current_node = queue.pop(0)
            if current_node:
                print(f"Traversed : {current_node.value}")
                traversed_nodes.append(current_node.value)
                queue.append(current_node.left)
                queue.append(current_node.right)
        print(f"BFS : {traversed_nodes}")
    # using the recursive appraoch for all DFS traversal
    def dfs_inorder(self):
        traversed_path=self._dfs_inorder_traversal(self.root,[])
        print(f"dfs inorder traversed path : {traversed_path}")

    def _dfs_inorder_traversal(self,current,traversed_nodes) -> list:
            if current.left:
                self._dfs_inorder_traversal(current.left,traversed_nodes)
            traversed_nodes.append(current.value)
            if current.right:
                self._dfs_inorder_traversal(current.right,traversed_nodes)
            return traversed_nodes

    def dfs_preorder(self):
        traversed_path=self._dfs_preorder_traversal(self.root,[])
        print(f"dfs preorder traversal path : {traversed_path}")

    def _dfs_preorder_traversal(self,current,traversed_nodes) -> list:
        traversed_nodes.append(current.value)
        if current.left:
            self._dfs_preorder_traversal(current.left,traversed_nodes)
        if current.right:
            self._dfs_preorder_traversal(current.right,traversed_nodes)
        return traversed_nodes

    def dfs_postorder(self):
        traversed_path = self._dfs_postorder_traversal(self.root, [])
        print(f"dfs postorder traversal path : {traversed_path}")

    def _dfs_postorder_traversal(self, current, traversed_nodes) -> list:
        if current.left:
            self._dfs_postorder_traversal(current.left, traversed_nodes)
        if current.right:
            self._dfs_postorder_traversal(current.right, traversed_nodes)
        traversed_nodes.append(current.value)
        return traversed_nodes

    def bstIsValid(self,root):
        self._helper(root)
        return self.isValid
    ## using in-order traversal to traverse the tree since we know it traverse in increasing order
    def _helper(self,currentNode):
        ## base condition
        if not currentNode: ## Equivalent to writing if currentNode is None:
            return

        self._helper(currentNode.left)
        if self.pre and self.pre.val >= currentNode.val:
            self.isValid=False
            return
        self.pre=currentNode
        self._helper(currentNode.right)













