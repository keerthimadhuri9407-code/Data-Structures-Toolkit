class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print(f"{self.stack.pop()} popped from stack")

    def display(self):
        print("Stack:", self.stack)


# -------- Queue Implementation --------
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print(f"{self.queue.pop(0)} removed from queue")

    def display(self):
        print("Queue:", self.queue)


# -------- Linear Search --------
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# -------- Main Program --------
if __name__ == "__main__":
    print("=== Data Structures Toolkit ===")

    # Stack demo
    s = Stack()
    s.push(10)
    s.push(20)
    s.pop()
    s.display()

    # Queue demo
    q = Queue()
    q.enqueue(5)
    q.enqueue(15)
    q.dequeue()
    q.display()

    # Searching demo
    arr = [3, 6, 9, 12, 15]
    key = 9
    result = linear_search(arr, key)

    if result != -1:
        print(f"{key} found at index {result}")
    else:
        print(f"{key} not found")