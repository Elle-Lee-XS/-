class Node:
    def __init__(self, value=None):
        self.value = value #这个node的值
        self.nextnode = None #这个node所指向的下一个node的地址

class LinkedList:
    def __init__(self):
        self.head = None #首先要定义链表的head，在声明之后，定义为Node
        """
        example:
        example_llist = LinkedList() #声明链表
        example_llist.head = Node(1) #声明这个链表的head是值为1的node
        node2 = Node(2) 
        node3 = Node(3)
        example_llist.head.nextnode = node2 #连接head与node2，head的nextnode储存的为node2的地址，利用example_llist.head.nextnode.value可查询值
        node2.nextnode = node3
        """
    
    def append(self, newnode): #定义一个增加链表元素的函数
        NewNode = Node(newnode)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
