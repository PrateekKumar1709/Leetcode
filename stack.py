class Stack():
    def __init__(self) -> None:
        self.items = []
            
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        self.items == []
    
    def list_items(self):
        return self.items
    
    def top_item(self):
        if not self.is_empty():
            return self.items[-1]    
        
myStack = Stack()
myStack.push("A")
print(myStack.list_items())
myStack.push("B")
print(myStack.list_items())
myStack.pop()
print(myStack.list_items())
print(myStack.top_item())

        