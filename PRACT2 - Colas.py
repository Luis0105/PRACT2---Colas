class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

    def get_info(self):
        return self.info

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class Queue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.top is None

    def front(self):
        if self.is_empty():
            return None
        return self.top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.get_info()
        self.top = self.top.get_next()
        if self.top is None:
            self.tail = None
        self.size -= 1
        return info

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size}")

        node = self.top
        i = 1
        while node:
            print(f"   ** Element {i}")
            node.get_info().print()
            node = node.get_next()
            i += 1
        print("******************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self.size:
            return None
        node = self.top
        for _ in range(1, pos):
            node = node.get_next()
        return node.get_info()

class Queue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.top is None

    def front(self):
        if self.is_empty():
            return None
        return self.top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.get_info()
        self.top = self.top.get_next()
        if self.top is None:
            self.tail = None
        self.size -= 1
        return info

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size}")

        node = self.top
        i = 1
        while node:
            print(f"   ** Element {i}")
            node.get_info().print()
            node = node.get_next()
            i += 1
        print("******************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self.size:
            return None
        node = self.top
        for _ in range(1, pos):
            node = node.get_next()
        return node.get_info()

queue = Queue()

order1 = Order(20, "cust1")
order2 = Order(30, "cust2")
order3 = Order(40, "cust3")
order4 = Order(50, "cust3")

queue.enqueue(order1)
queue.enqueue(order2)
queue.enqueue(order3)
queue.enqueue(order4)

queue.print_info()

print("Front: ")
queue.front().print()

print("Dequeue: ")
queue.dequeue().print()

queue.print_info()

print("Get 2nd element: ")
queue.get_nth(2).print()