from inspect import stack
from stacks.stack import Stack
open_brackets = ["{", "[", "("]
closed_brakets = ["}", "]", ")"]

def valiate_brackets(string):
    balanced = 'true'
    str_len = len(string)
    for i in range(str_len):
        # print(string[i])
        if string[i] in open_brackets:
            bracketStack.push(string[i])
        elif bracketStack.is_empty():
            balanced = "false"
            break
        else:
            bracketStack.pop()
            
    if bracketStack.is_empty() and balanced == 'true':
        print("The given String is balanced")
    else:
        print("Given string is unbalanced")      

string = "{[()}]{{}}"

bracketStack = Stack()
valiate_brackets(string)




        
    