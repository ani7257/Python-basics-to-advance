#Problem2
class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []
    
    def get_occupied_table_list(self):
        return self.occupied_table_list
    
    def allocate_table(self):
        if not self.occupied_table_list:
            self.occupied_table_list.append(1)
        else:
            for i in range(len(self.occupied_table_list)):
                if i == len(self.occupied_table_list)-1:
                    if self.occupied_table_list[i] != 10:
                        self.occupied_table_list.append(self.occupied_table_list[i]+1)
                        break
                elif self.occupied_table_list[i+1] - self.occupied_table_list[i] > 1:
                    self.occupied_table_list.insert(i+1, self.occupied_table_list[i]+1)
                    break
    
    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="\n")
            current_node = current_node.next
            
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_list()
print("Reverse List:")
linked_list.reverse()
linked_list.print_list()


    
        
    
