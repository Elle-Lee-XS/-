class Node:
    def __init__(self, value=None):
        self.value = value #这个node的值
        self.nextnode = None #这个node所指向的下一个node的地址

class LinkedList:
    def __init__(self):
        self.head = None #首先要定义链表的head，在声明之后，定义为Node
        """
        example:
        example_llist = LinkList() #声明链表
        example_llist.head = Node(1) #声明这个链表的head是值为1的node
        node2 = Node(2) 
        node3 = Node(3)
        example_llist.head.nextnode = node2 #连接head与node2，head的nextnode为node2的地址
        node2.nextnode = node3
        """
    def Append(self, value): # 遍历列表 并在链表最后增加一个元素
        NewNode = Node(value)
        if self.head is None: # 如果这个链表没有head，增加新元素为head
            self.head = NewNode
            return
        current_node = self.head
        while(current_node.nextnode): # 当 当前node一直有下一个元素的时候 我们进行循环 直到我们循环到最后一个元素 指向nextnode的地址为None 出循环
            current_node = current_node.nextnode
        current_node.nextnode = NewNode # 更新旧列表的下一个元素为新增元素
        
    def PrintLinkedList(self): # 打印这个链表
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.nextnode
            
    def AddAsHead(self, value): #添加新元素为head
        NewNode = Node(value)
        previous_head = self.head 
        self.head = NewNode #只需将旧head替换为新的head，并指向旧head就行
        self.head.nextnode = previous_head
