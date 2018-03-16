class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def insert_at_start(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def insert_between(self, previousNode, data):
        if previousNode.next is None:
            print('Previous node should have next node')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode

    def insert_at_end(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp = temp.next

    def delete(self, data):
        temp = self.head
        if temp.next is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
            else:
                # search all nodes
                while temp.next != None:
                    if temp.data == data:
                        break
                    prev = temp
                    temp = temp.next

                if temp == None:
                    return

                prev.next = temp.next
                return
    def search(self, node, data):
        if node == None:
            return False

        if node.data == data:
            return True

        return self.search(node.get_next(), data)

if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)
    node2 = Node(2)
    List.head.set_next(node2)
    node3 = Node(3)
    node2.set_next(node3)
    List.insert_at_start(4)
    List.insert_between(node2, 5)
    List.insert_at_end(6)
    List.print_linked_list()
    print()
    List.delete(3)
    List.print_linked_list()
    print()
    print(List.search(List.head, 1))