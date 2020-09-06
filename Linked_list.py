class Node:
    def __init__(self, value=None):
        self.value = value # 这个node的值
        self.nextnode = None # 这个node所指向的下一个node的地址

class LinkedList:
    def __init__(self):
        self.head = None # 首先要定义链表的head，在声明之后，定义为Node
        """
        example:
        example_llist = LinkedList() # 声明链表
        example_llist.head = Node(1) # 声明这个链表的head是值为1的node
        node2 = Node(2) 
        node3 = Node(3)
        example_llist.head.nextnode = node2 # 连接head与node2，head的nextnode储存的为node2的地址，利用example_llist.head.nextnode.value可查询值
        node2.nextnode = node3
        """
    
    def append(self, value): # 在链表最后增加一个元素
        NewNode = Node(value)
        if self.head is None: # 如果这个链表没有head，增加新元素为head
            self.head = NewNode
        current_node = self.headval
        while(current_node.nextval): # 当 当前node一直有下一个元素的时候 我们进行循环 直到我们循环到最后一个元素 指向nextnode的地址为None 出循环
            current_node = laste.nextval
        current_node.nextval = NewNode # 更新旧列表的下一个元素为新增元素
