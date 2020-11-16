class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
  
  def get_value(self):
    return self.data

  def get_next(self):
    return self.next
  
  def set_next(self, new_next):
    self.next = new_next
    

class LinkedList:
  def __init__(self, first_node = None):
    self.head = first_node
    self.tail = first_node
  
  def add_to_head(self, value):
    #Create a new node
    new_node = Node(value)
    # If there are no nodes...
    if self.head is None:
      # set head to new node
      self.head = new_node
      # set tail to new node
      self.tail = new_node
    else:
      # set next_node of my new Node to old head
      new_node.set_next(self.head)
      #Update head attr
      self.head = new_node
  
  def add_to_tail(self, data):
    # Create a new node
    new_node = Node(data)
    # If list is empty
    if self.head is None:
      # update head & tail attr
      self.head = new_node
      self.tail = new_node

    # If list not empty
    else:
      #update next_node of tail
      self.tail.set_next(new_node)
      # Update self.tail
      self.tail = new_node
      
      
  def remove_head(self):
    # Empty List
    if self.head is None:
      return None
    # return value of the old head
    else:
      # capture the return value
      ret_value = self.head.get_value()
      # List with one element
      if self.head is self.tail:
        self.head = None
        self.tail = None
        # List with 2+ elements
      else:
        self.head = self.head.get_next()
    return ret_value
  
  
  def remove_tail(self):
    if self.tail is None:
      return None
    else:
      ret_value = self.tail.get_value()
      if self.head == self.tail:
        self.head = None
        self.tail= None
      else:
        itr = self.head
        while itr:
          prev = itr
          itr = itr.get_next()
          if itr == self.tail:
            self.tail = prev
      return ret_value
    
  def contains(self, value):
    #Loop through LL til next pointer is none
    cur_node = self.head
    while cur_node is not None:
      # if we find value
      if cur_node.get_value() == value:
        return True
      cur_node = cur_node.get_next()
    # return False
    return False
  
  def get_max(self):
    pass