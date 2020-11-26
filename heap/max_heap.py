class Heap:
    def __init__(self):
        self.storage = []
        
    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2
    
    def get_parent_index(self, child_index):
        return (child_index - 1) // 2
    
    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.storage) - 1
    
    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.storage) - 1
    
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    
    def left_child(self,index):
        return self.storage[self.get_left_child_index(index)]
    
    def right_child(self,index):
        return self.storage[self.get_right_child_index(index)]
    
    def parent(self,index):
        return self.storage[self.get_parent_index(index)]
    
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    
    def insert(self, value):
       self.storage.append(value)
       self._bubble_up(len(self.storage)-1)

    def delete(self):
        if len(self.storage) == 0:
            raise Exception('Heap is empty.')
        else:
            temp = self.storage[0]
            self.storage[0] = self.storage[-1]
            del self.storage[-1]
            self._sift_down(0)
            return temp

    def get_max(self):
        if len(self.storage) == 0:
            raise Exception('Heap is empty.')
        else:
            return self.storage[0]
            
    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while self.has_parent(index) and self.parent(index) < self.storage[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def _sift_down(self, index):
        while self.has_left_child(index):
            larger_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                larger_index = self.get_right_child_index(index)
                
            if self.storage[index] > self.storage[larger_index]:
                break
            else:
                self.swap(index, larger_index)
            
            index = larger_index
            

# pile = Heap()

# pile.insert(12)
# print(pile.storage)
# pile.insert(14)
# print(pile.storage)
# pile.insert(10)
# print(pile.storage)
# pile.insert(56)
# print(pile.storage)
# pile.insert(22)
# print(pile.storage)
# pile.insert(20)
# print(pile.storage)
# pile.insert(200)
# print(pile.storage)
# pile.insert(19)
# print(pile.storage)
# pile.insert(130)
# print(pile.storage)
# pile.insert(100)
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)
# pile.delete()
# print(pile.storage)