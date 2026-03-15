from typing import Optional, Any, List
from collections import deque

class Node:
    """二叉树节点"""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None


class BinaryTree:
    """二叉树"""
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, value: Any):
        """插入节点"""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.left is None:
                node.left = new_node
                return
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = new_node
                return
            else:
                queue.append(node.right)


    def search(self, target_value: Any) -> Optional[Node]:
        """查找节点"""
        if self.root is None:
            return None

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.value == target_value: #最开始
                return node

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return None



    def delete(self, target_value: Any) -> bool:
        """删除节点(标记删除)"""
        if self.root is None:
            print("空二叉树，删除无意义")
            return False

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.value == target_value:
                node.value = None
                return True
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return False


    def preorder_traversal(self) -> List[Any]:
        """前序遍历"""
        def preorder(node:Node):
            if node is None:
                return
            res.append(node.value)
            preorder(node.left)
            preorder(node.right)

        res = []
        preorder(self.root)
        return res



    def inorder_traversal(self) -> List[Any]:
        """中序遍历"""
        def inorder(node:Node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.value)
            inorder(node.right)

        res = []
        inorder(self.root)
        return res

    def postorder_traversal(self) -> List[Any]:
        """后序遍历"""
        def postorder(node:Node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.value)

        res = []
        postorder(self.root)
        return res

    def level_order_traversal(self) -> List[Any]:
        """层序遍历"""
        res = []
        if self.root is None:
            return res

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            res.append(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return res


    def height(self) -> int:
        """树的高度"""
        if self.root is None:
            return 0

        queue = deque([self.root])
        height = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            height += 1
        return height
    '''
    #更简单的实现
    def height(self) -> int:
        def _height(node: Optional[Node]) -> int:
            if node is None:
                return 0
            return max(_height(node.left), _height(node.right)) + 1
        return _height(self.root)
    '''


    def is_empty(self) -> bool:
        """检查树是否为空"""
        return self.root is None


# ---------- 测试示例 ----------
if __name__ == '__main__':
    # 创建二叉树实例
    tree = BinaryTree()
    print("树是否为空?", tree.is_empty())  # True

    # 插入节点
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    print("插入节点: 10, 5, 15")

    print("树是否为空?", tree.is_empty())  #False

    # 查找节点
    treenode = tree.search(5)
    print("查找节点5:", treenode)

    # 删除节点
    deleted = tree.delete(10)
    print("删除节点10:", deleted)

    # 遍历
    print("前序遍历:", tree.preorder_traversal())
    print("中序遍历:", tree.inorder_traversal())
    print("后序遍历:", tree.postorder_traversal())
    print("层序遍历:", tree.level_order_traversal())

    # 树高度
    print("树的高度:", tree.height())  # 输出 None（因未实现）

    # 如果需要更具体的测试，可以手动构造树来展示预期行为
    # 手动构造一个树用于测试（仅为演示）
    print("\n--- 手动构造树测试 ---")
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    # 遍历函数尚未实现，手动遍历示例（实际应调用方法）
    print("手动构造的树根节点值:", tree.root.value)  # 1
    print("左子节点值:", tree.root.left.value)       # 2
    print("右子节点值:", tree.root.right.value)      # 3

