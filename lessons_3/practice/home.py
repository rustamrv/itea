

class Stack:

    def __init__(self):
        self.my_stack = []

    def push(self, num):
        self.my_stack.append(num)

    def pop(self):
        return self.my_stack.pop()


class Qu

class Stack:

    def __init__(self):
        self.my_stack = []

    def push(self, num):
        self.my_stack.append(num)

    def pop(self):
        return self.my_stack.pop()


class Queues:

    def __init__(self):
        self.my_queue = []

    def push(self, num):
        self.my_queue.append(num)

    def pop(self):
        return self.my_queue.pop(0)


class Complex:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b if b > 0 else b*-1
        self.symbol = "+" if b >= 0 else "-"

    def __str__(self):
        if self.a == 0:
            return f'{self.b}i'
        return f'{self.a} {self.symbol} {self.b}i'


if __name__ == "__main__":
    print("stack")
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    print(stack.pop())
    print(stack.my_stack)
    print(stack.pop())
    print(stack.my_stack)
    print("queue")
    queue = Queues()
    queue.push('a')
    queue.push('b')
    queue.push('c')
    print(queue.pop())
    print(queue.my_queue)
    print(queue.pop())
    print(queue.my_queue)
    print("complex")
    c = Complex(5, 6)
    print(c)
    v = Complex(2, -3)
    print(v)
    v = Complex(1)
    print(v)
    v = Complex()
    print(v)

