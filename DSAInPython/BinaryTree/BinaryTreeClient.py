from BST import BST

class BinaryTreeClient:
    if __name__ == "__main__":
        bst=BST()
        bst.insert(5)
        bst.insert(4)
        bst.insert(7)
        bst.insert(2)
        bst.insert(6)
        bst.insert(8)

        # bst.look_up(7)
        # bst.look_up(6)
        print("Initial BST")
        bst.print_tree()

        # print("Case 1: Node has no children( leaf node)")
        # bst.delete(2)
        # bst.print_tree()

        # print("Case 2: Node has one children")
        # bst.delete(4)
        # bst.print_tree()

        print("Case 3 : Node has two children")
        bst.delete(7)
        bst.print_tree()

        # print("BFS Traversal")
        # bst.bfs_traversal()
        # print("dfs inorder traversal")
        # bst.dfs_inorder()
        # print("dfs preorder traversal")
        # bst.dfs_preorder()
        # print("dfs post order traversal")
        # bst.dfs_postorder()

