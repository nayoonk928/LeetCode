class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
        

    def push(self, x: int) -> None:
        self.stack_push.append(x)
        

    def pop(self) -> int:
        # pop 스택이 비어있다면 push 스택을 pop 스택으로 복사
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        
        # pop 스택이 비어있다 = 큐가 비어있다
        if not self.stack_pop:
            return -1
        
        return self.stack_pop.pop()
        

    def peek(self) -> int:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        
        if not self.stack_pop:
            return -1
        
        return self.stack_pop[-1]

    def empty(self) -> bool:
        return not (self.stack_push or self.stack_pop)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()