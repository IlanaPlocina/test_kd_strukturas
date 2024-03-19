class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

def findInStack(stack, x):
    found = False
    temp_stack = Stack()  # Pagaidu kaudze, lai saglabātu kaudzes stāvokli

    # Pārbauda katru elementu kaudzē, lai atrastu 'x'
    while not stack.isEmpty():
        item = stack.pop()
        temp_stack.push(item)  # Saglabā elementu pagaidu kaudzē
        if item == x:
            found = True
            break

    # Atgriež kaudzes sākotnējo stāvokli
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())

    return found

def loadValuesFromFile(filename, stack):
    try:
        with open(filename, 'r') as file:
            values = file.readline().split() 
            for value in values:
                stack.push(int(value))  
    except FileNotFoundError:
        print(f"Failu '{filename}' nevar atrast.")



myStack = Stack()
filename = "values.txt"  
loadValuesFromFile(filename, myStack)


elementToFind = 1
isElementFound = findInStack(myStack, elementToFind)
print(isElementFound)

