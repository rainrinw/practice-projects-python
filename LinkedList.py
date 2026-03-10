class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
#在链表开头插入新节点
    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node


#在链表尾部增加节点
    def insert_at_end(self, data):

        node = Node(data)
        if self.head is None:
            self.head = node
            print(f"{node}是第一个元素")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

#打印所有节点的数据
    def display(self):

        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


#删除包含指定数据的节点
    def delete(self, target_data):


        if self.head is None:
            return

        if target_data == self.head.data:
            self.head = self.head.next
            return

        curr = self.head.next
        prev = self.head

        while curr is not None:
            if curr.data == target_data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        return

#查找指定数据是否存在，如果存在则打印指定数据，返回布尔值
    def search(self, target_data):
        current = self.head
        while current is not None:
            if current.data == target_data:
                return True
            current = current.next
        return False

    #返回链表的长度
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    # 测试例子：创建链表并调用基础方法
    ll = LinkedList()
    print("链表已创建")

    # 插入操作
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)

    # 显示链表
    ll.display()

    # 查找节点
    found = ll.search(20)
    print(f"查找20: {found}")

    # 删除节点
    ll.delete(10)

    # 获取大小
    print("链表大小:", ll.size())