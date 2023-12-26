class Jar:
    def __init__(self, capacity=12):
        if not (isinstance(capacity, int) and capacity > 0):
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("OverLoaded")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("too many 🍪s withdrawed")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        if not (isinstance(value, int) and value > 0):
            raise ValueError("NOT a valid capacity")
        self._capacity = value

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if self.capacity < self._size < 0:
            raise ValueError("from size setter")
        self._size = value


    
    

if __name__ == "__main__":
    jar = Jar()
