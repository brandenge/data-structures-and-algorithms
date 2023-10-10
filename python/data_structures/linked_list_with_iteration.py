class Node:
  
    def __init__(self, data = None):
        self.data = data
        self.next = None


    def __str__(self):
        return f'Node({self.data})'


class LinkedListWithIteration:

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0


    def append(self, data):
        node = Node(data)
        if self.tail: self.tail.next = node
        if self.head is None: self.head = node
        self.tail = node
        self._length += 1
        return node.data


    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail is None: self.tail = node
        self._length += 1
        return node.data


    def last(self):
        if not self.tail: return None
        return self.tail.data
  
  
    def count(self):
        return self._length


    def has_cycle(self):
        nodes = {}
        current = self.head

        while current:
            if current in nodes: return True
            nodes[current] = True
            current = current.next

        return False

  
    def to_array(self, nodes = False):
        if self.has_cycle(): raise LinkedListCycleError
        array = []
        current = self.head

        while current:
            array += ([current] if nodes else [current.data])
            # also stop at the tail, in the case the list a subset of another list after the tail
            if current == self.tail: break
            current = current.next

        return array


    def __str__(self):
        if self._length == 0: return 'The linked list is empty'
        if type(self.head) != type(Node()): return str(self.head)

        nodes = {}
        list_string = ''
        current = self.head
        print('current is', current)

        while type(current) == type(Node()):
            if current is self.head: list_string += f'Head({str(current)})'
            elif current is self.tail: list_string += f'Tail({str(current)})'
            else: list_string += str(current)
            list_string += ' -> '
            if current in nodes: break
            nodes[current] = True
            current = current.next

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
        current = self.head
        counter = 0

        while current:
            if current.data == data: counter += 1
            current = current.next

        return counter
  
  
    def find_index_of(self, data):
        if self.has_cycle(): raise LinkedListCycleError
        current = self.head
        index = 0
      
        while current:
            if current.data == data:
                return index

            current = current.next
            index += 1

        return None

  
    def find_value_at(self, index):
        if self.has_cycle(): raise LinkedListCycleError
        current = self.head
        counter = 0

        while current:
            if index == counter:
                return current.data

            current = current.next
            counter += 1

        return None

  
    def insert_at_position(self, index, data):
        if self.has_cycle(): raise LinkedListCycleError
        if index == 0: return self.prepend(data)
        if index == self._length: return self.append(data)
        if index > self._length or index < 0: return None
        node = Node(data)
        counter = 0
        current = self.head
      
        while current:
            if counter + 1 == index:
                node.next = current.next
                current.next = node
                break
            current = current.next
            counter += 1
          
        if not self.tail: self.tail = node
        self._length += 1
        return node.data


    def delete_at_position(self, index):
        if self.has_cycle(): raise LinkedListCycleError
        if index < 0 or index >= self._length: return None             
        node = None
        if index == 0:
            node = self.head
            self.head = self.head.next
      
        current = self.head
        counter = 0

        while current and not node:
            if counter + 1 == index:
                node = current.next
                current.next = current.next.next
              
                if self.tail == node:
                    self.tail = current
                    self.tail.next = None
                    
            counter += 1
            current = current.next

        if node:
            self._length -= 1
          
            if self._length == 0:
                self.head = None
                self.tail = None
          
            return node.data


    def delete_value(self, data):
        index = self.find_index_of(data)
        if index is None: return None
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
      
        current = self.head
        counter = 0

        while current:
            if counter == index - 1:
                list.tail.next = current.next
                current.next = list.head
                break

            counter += 1
            current = current.next

        return self


    def reverse(self):
        if self.has_cycle(): raise LinkedListCycleError
        if self._length < 2: return self
        # the list cannot be a subset of another list after the tail, or else it will create a cycle
        if self.tail.next is not None: raise LinkedListCycleError
      
        current = self.head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

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