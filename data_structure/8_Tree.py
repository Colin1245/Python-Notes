"""Python二叉树的前序遍历、中序遍历、后序遍历"""

class TreeNode(object):
    def __init__(self, elem = -1, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self, root = None):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

#深度优先遍历
    def preorder(self, root):
        """递归实现前序遍历"""
        if root == None:
            return
        print(root.elem, end= " ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem, end= " ")
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end= " ")


if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    print("\n")
    t.preorder(t.root)
    print("\n")
    t.inorder(t.root)
    print("\n")
    t.postorder(t.root)

