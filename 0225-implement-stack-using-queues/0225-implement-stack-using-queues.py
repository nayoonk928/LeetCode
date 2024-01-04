class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        # 큐의 크기만큼 반복하면서 순서 뒤집기
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        if not self.empty():
            return self.queue.popleft()
        

    def top(self) -> int:
        if not self.empty():
            return self.queue[0]
        

    def empty(self) -> bool:
        return not bool(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()