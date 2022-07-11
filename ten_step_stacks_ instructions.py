import time

# create the node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

# create the stack class
class Stack:
    def __init__(self, limit=10):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("The stack is full")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("The stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("The stack is empty")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

ten_steps = Stack()

review_mode = False

for x in range(ten_steps.limit):
    if ten_steps.size == 0:
        print("""### Welcome to the instructions creator ### 
Create a list of instructions and then view them""")
        print()
        first_step = input("Please add the first step of your instructions: ")
        ten_steps.push(first_step)
    else:
        print()
        choice = input("Would you like to a add another step? (y/n): ")
        if choice.lower().strip() == "y":
            enter_step = input("Please input step " + str(ten_steps.size + 1) + ": ")
            ten_steps.push(enter_step)
        if choice.lower().strip() == "n":
            break
        else:
            pass

# create a new pile for finished instructions
instructions_pile = Stack()

# put the pile from the instruction list onto the new file so number one is first again...
for temp in range(int(ten_steps.size)):
    instructions_pile.push(ten_steps.pop())

def review_notes():
    for temp in range(int(instructions_pile.size)):
        current_item = instructions_pile.pop()
        ten_steps.push(current_item)
        print("Step " + str(ten_steps.size) + ": " + current_item)
        time.sleep(0.5)

    for temp in range(int(ten_steps.size)):
        instructions_pile.push(ten_steps.pop())

    start_review()

def start_review():
    print()
    review = input("Would you like to view the instructions? (y/n) ")
    if review == "y":
        print()
        review_notes()
    if review == "n":
        exit()
    else:
        start_review()

start_review()