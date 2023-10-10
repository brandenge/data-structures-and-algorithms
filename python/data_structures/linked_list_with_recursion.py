class Node:
  
    def __init__(self, data = None):
        self.data = data
        self.next = None

  
    def append(self, data):
        if self.next is None:
            node = Node(data)
            self.next = node
            return node

        return self.next.append(data)
  
  
    def count(self, counter):
        if self.next is None: return 0
        return 1 + self.next.count()


    def has_cycle(self, nodes):
        if self in nodes: return True
        if type(self.next) != type(Node()): return False
        nodes[self] = True
        return self.next.has_cycle(nodes)


    def to_array(self, array, tail, nodes):
        array += ([self] if nodes else [self.data] )
        # also stop at the tail, in the case the list a subset of another list after the tail
        if type(self.next) != type(Node()) or self is tail: return array
        return self.next.to_array(array, tail, nodes)
      

    def count_value(self, data, tail):
        if type(self) != type(Node()): return 0
        is_countable = self.data == data
        if type(self.next) != type(Node()) or self is tail: return (1 if is_countable else 0)
        return (1 if is_countable else 0) + self.next.count_value(data, tail)


    def find_index_of(self, index, data, tail):
        if self.data == data: return index
        if self.next is None or self is tail: return
        return self.next.find_index_of(index + 1, data, tail)


    def find_value_at(self, index, tail):
        if index == 0: return self.data
        if index < 0 or self.next is None or self is tail: return
        return self.next.find_value_at(index - 1, tail)


    def find_prev_node_of_index(self, index, tail):
        if index == 1: return self 
        if type(self.next) != type(Node()) or self is tail: return
        return self.next.find_prev_node_of_index(index - 1, tail)
  
  
    def insert_at_position(self, index, data, tail):
        if index == 0:
            node = Node(data)
            node.next = self.next
            self.next = node
            return data

        if index < 0 or self.next is None or self is tail: return
        return self.next.insert_at_position(index - 1, data, tail)
        

    def delete_at_position(self, index, tail):
        if index == 0: return [None, self]
        if index == 1:
            prev_node = self
            deleted_node = self.next
            self.next = self.next.next
            return [prev_node, deleted_node]

        return self.next.delete_at_position(index - 1, tail)


    def reverse(self, prev):
        next = self.next
        self.next = prev
        if type(next) != type(Node()): return
        next.reverse(self)
  

    def __str__(self):
        return f'Node({self.data})'


    def _list_to_str(self, head, tail, nodes, string = ''):
        if self is head: string += f'Head({str(self)})'
        elif self is tail: string += f'Tail({str(self)})'
        else: string += str(self)
        string += ' -> '

        if self in nodes or type(self) != type(Node()) or type(self.next) != type(Node()):
            return string
          
        nodes[self] = True
        return self.next._list_to_str(head, tail, nodes, string)


class LinkedListWithRecursion:
  
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0


    def append(self, data):
        self._length += 1
      
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return data

        appended_node = self.head.append(data)
        self.tail = appended_node
        return data


    def prepend(self, data):
        self._length += 1
        node = Node(data)
        node.next = self.head
        self.head = node
        return data

    def last(self):
        if self.tail == None: return
        return self.tail.data

  
    def count(self):
        return self._length


    def has_cycle(self):
        if self._length == 0: return False
        if type(self.head) != type(Node()): return False
        return self.head.has_cycle({})

  
    def to_array(self, nodes = False):
        if self.has_cycle(): raise LinkedListCycleError
        array = []
        if self._length == 0: return array
        return self.head.to_array(array, self.tail, nodes)
  

    def __str__(self):
        if self._length == 0: return 'The linked list is empty'

        if type(self.head) != type(Node()): return str(self.head)
        list_string = self.head._list_to_str(self.head, self.tail, {})

        if type(self.tail) == type(Node()): list_string += str(self.tail.next)
        else: list_string += 'N/A'
      
        return list_string

  
    def print_state(self):
        message = ''
        message += f'the list looks like: {self}\n\n'
        message += f'self._length is: {self._length}\n\n'
        message += f'self.head is: {self.head}\n'
        message += f'self.tail is: {self.tail}\n'
                    
        if type(self.head) == type(Node()): 
            message += f'self.head.next is: {self.head.next}\n'
        else:
            message += f'self.head.next is: N/A\n'

        if type(self.tail) == type(Node()):
            message += f'self.tail.next is: {self.tail.next}\n'
        else:
            message += f'self.tail.next is: N/A\n'

        print(message)
  
  
    def is_valid(self):      
        if self._length == 0:
            if self.head != None or self.tail != None:
                print('The list is empty but the head and/or tail is not equal to None. ')
                self.print_state()
                return False
            return True
      
        if type(self.head) != type(Node()) and self.head != None:
            print('The head is the wrong data type - it must be either a Node or None. ')
            self.print_state()
            return False
      
        if type(self.tail) != type(Node()) and self.tail != None:
            print('The tail is the wrong data type - it must be either a Node or None. ')
            self.print_state()
            return False
      
        if (self._length > 0 and 
            self.tail != None and 
            type(self.tail.next) != type(Node()) and 
            self.tail.next != None):
            print('The tail and/or tail.next is the wrong data type - both must be either a Node or None. ')
            self.print_state()
            return False

        if self.has_cycle():
            print('The linked list is not valid because it has a cycle in it. ')
            self.print_state()
            return False

        array = self.to_array()

        if len(array) != self._length:
            print(f'The length of the list: {self._length} does not match the number of nodes: {len(array)}. ')
            self.print_state()
            return False
      
        if len(array) > 0:
            if self.head.data != array[0]:
                print('The head is not pointing to the correct node. ')
                self.print_state()
                return False

            if self.tail != None and self.tail.data != array[-1]:
                print('The tail is not pointing to the correct node. ')
                self.print_state()
                return False

        return True


    def count_value(self, data):
        if self.has_cycle(): raise LinkedListCycleError
        if self.head is None: return 0
        return self.head.count_value(data, self.tail)
  
  
    def find_index_of(self, data):
        if self.has_cycle(): raise LinkedListCycleError
        if self.head is None: return
        return self.head.find_index_of(0, data, self.tail)

  
    def find_value_at(self, index):
        if self.has_cycle(): raise LinkedListCycleError
        if self.head is None: return
        return self.head.find_value_at(index, self.tail)


    def find_prev_node_of_index(self, index):
        if index < 1 or index >= self._length: return
        if type(self.head) != type(Node()): return
        return self.head.find_prev_node_of_index(index, self.tail)
    
  
    def insert_at_position(self, index, data):
        if self.has_cycle(): raise LinkedListCycleError
        if index == 0: return self.prepend(data)
        if index == self._length: return self.append(data)
        if index < 0 or index > self._length: return
        self._length += 1
        return self.head.insert_at_position(index, data, self.tail)


    def delete_at_position(self, index):
        if self.has_cycle(): raise LinkedListCycleError
        if index < 0 or index >= self._length: return
        if type(self.head) != type(Node()): return
              
        prev_node, deleted_node = self.head.delete_at_position(index, self.tail)
      
        if index == 0:
            self.head = self.head.next
        if index == self._length - 1:
            self.tail = prev_node
          
        self._length -= 1
        return deleted_node.data


    def delete_value(self, data):
        index = self.find_index_of(data)
        if index is None: return
        if type(self.head) != type(Node()): return
        return self.delete_at_position(index)


    def insert_list(self, index, list):
        if self.has_cycle() or list.has_cycle(): raise LinkedListCycleError
        if list._length == 0 or index < 0 or index > self._length: return self
        self._length += list._length
          
        if 0 == self._length:
            self.head = list.head
            self.tail = list.tail
            return self

        if index == 0:
            list.tail.next = self.head
            self.head = list.head
            return self
          
        if index == self._length:
            self.tail.next = list.head
            self.tail = list.tail
            return self

        prev_node = self.find_prev_node_of_index(index)
        list.tail.next = prev_node.next
        prev_node.next = list.head

        return self


    def reverse(self):
        if self.has_cycle(): raise LinkedListCycleError
        if self._length < 2: return self
        if type(self.head) != type(Node()): return self
        # the list cannot be a subset of another list after the tail, or else it will create a cycle
        if self.tail.next is not None: raise LinkedListCycleError
      
        current = self.head
        prev = None
        current.reverse(prev)

        self.head, self.tail = self.tail, self.head
        return self

  
    def sort(self):
        if self.has_cycle(): raise LinkedListCycleError
        array = self.to_array()
        array.sort()
        list = self.__class__()
      
        for element in array:
            list.append(element)

        return list


class LinkedListCycleError(Exception):
    """
    Exception raised when the linked list has a cycle.
    """
  
    def __init__(self):
        self.message = "The linked list has a cycle causing an infinite loop for traversal."
        super().__init__(self.message)