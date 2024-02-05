from queue import Queue

class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def push(self, x: int) -> None:
        self.queue1.put(x)
    
    #FIFO, queue1과 2가 서로 옮겨져도 그 성질이 유지된다.
    def pop(self) -> int:
        if self.empty():
            print("Stack is empty")
            return None

        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        popval = self.queue1.get()
        
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popval
            
    #pop과 top은 FIFO구조에서 뺀 값을 다시 put하는 여부의 차이이다.
    def top(self) -> int:
        topval = self.pop()
        self.queue1.put(topval)
        
        return topval

    def empty(self) -> bool:
        return self.queue1.empty() and self.queue2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()