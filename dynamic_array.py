class DynamicArray:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.array = [0] * capacity

    # Get the elemnent at index i.
    def get(self, i: int) -> int:
        return self.array[i]

    # Set the element at index i to n.
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # Push the elment n to the end of the array
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    # Pop and return the elemnt at the end of the array
    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        # Return the popped element
        return self.array[self.size]

    # Double the capacity of the array
    def resize(self) -> None:
        # Create a new array with double the capacity
        new_capacity = self.capacity * 2
        new_array = [0] * new_capacity
        # Copy the elements to the new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_capacity

    # Return the number of elements in the array
    def getSize(self) -> int:
        return self.size
    
    # Return the capacity of the array
    def getCapacity(self) -> int:
        return self.capacity
