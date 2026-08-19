class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        if i < self.length and self.length <= self.capacity:
            return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if i < self.length and self.length <= self.capacity:
            self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length <= self.capacity:
            self.arr[self.length - 1] = n

        else:
            self.arr.resize()
            self.arr[self.length - 1] = n

    def popback(self) -> int: 
        return self.arr.pop()

 

    def resize(self) -> None:
        new_arr = [0] * capacity * 2
        for i in range(len(arr)):
            new_arr[i] = arr[i] 
        


    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.capacity
