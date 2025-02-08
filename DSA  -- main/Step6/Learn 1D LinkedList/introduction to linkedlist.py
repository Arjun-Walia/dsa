class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def lengthNode(self):
        current_node = self.head
        cnt = 0
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt

    def printNode(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print(None)

    def extractIndex(self, index):
        if index >= self.lengthNode():
            return "index out of range"
        curIndex = 0
        current_node = self.head
        while current_node:
            if curIndex == index:
                return current_node
            curIndex += 1
            current_node = current_node.next
            
    def insert(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def erase(self, index):
        if index >= self.lengthNode():
            return "index out of range"
        current_node = self.head
        if index == 0:
            self.head = current_node.next
            return
        prev_node = None
        curIndex = 0
        while current_node:
            if curIndex == index:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
            curIndex += 1
        
l = [1, 2, 3, 4, 5]
linked_list = LinkedList()
for i in l:
    linked_list.append(i)

linked_list.printNode()
print(linked_list.lengthNode()) 
node = linked_list.extractIndex(4)
print(node.data if node != "index out of range" else node)  
new = linked_list.erase(1)
linked_list.insert(100)
linked_list.printNode()