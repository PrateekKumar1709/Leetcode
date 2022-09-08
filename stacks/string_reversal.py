from stacks.stack import Stack

def str_reversal (string):
    rev_str=""
    for i in range(len(string)):
        myStack.push(string[i])
    for i in range(len(string)):
        rev_str = rev_str + (myStack.pop())
    print(rev_str)    
        
myStack = Stack()
str_reversal("String")

