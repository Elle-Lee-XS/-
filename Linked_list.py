class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextvalue = None 

class SLinkedList:
    def __init__(self):
        self.headvalue = None
    
    def append(self, newdata): #增加链表元素
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
