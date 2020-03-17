from array import array


class Array:
    def __init__(self, data_type, *items):
        self.data = array(data_type, items)

    def __iter__(self):
        return self.MyIter(self.data)

    def __contains__(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return True
            return False

    def __len__(self):
        return len(self.data)

    def __reversed__(self):
        return self.MyIter(self.data, direction=-1)

    def __getitem__(self, item):
        if isinstance(item, slice):
            raise TypeError("Expected type 'int', got type 'slice' of attr item")
        return self.data[item]

    def index(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return i
        return -1

    def count(self, item):
        return sum([1 for i in self if i == item])

    class MyIter:
        def __init__(self, collection, direction=1):
            self.collection = collection
            self.direction = direction
            if direction == 1:
                self.position = -1
                self.step = 1
            else:
                self.position = len(self.collection)
                self.step = -1

        def __next__(self):
            if self.position + 1 >= len(self.collection) and self.step == 1 or \
                    self.position - 1 <= 0 and self.step == -1:
                raise StopIteration()
            self.position += self.step
            return self.collection[self.position]

        def __iter__(self):
            return self

