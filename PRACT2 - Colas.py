class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_info(self):
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


class LinkedQueue:
    def __init__(self):
        self.top = None  # La cabeza de la cola
        self.tail = None  # El último nodo de la cola
        self.size = 0  # Para llevar la cuenta del número de elementos

    def is_empty(self):
        return self.top is None

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.next
        self.size -= 1
        if self.top is None:  # Si la cola queda vacía
            self.tail = None
        return info

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def size(self):
        return self.size

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"Size: {self.size}")
        node = self.top
        index = 1
        while node is not None:
            print(f"   ** Element {index}")
            node.info.print_info()  # Llama al método print_info de Order
            node = node.next
            index += 1
        print("******************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self.size:
            return None
        current = self.top
        for _ in range(1, pos):
            current = current.next
        return current.info


class TestQueue:
    @staticmethod
    def main():
        queue = LinkedQueue()

        # Crear pedidos
        order1 = Order(20, "cust1")
        order2 = Order(30, "cust2")
        order3 = Order(40, "cust3")
        order4 = Order(50, "cust4")

        # Insertar pedidos en la cola
        queue.enqueue(order1)
        queue.print_info()

        queue.enqueue(order2)
        queue.print_info()

        queue.enqueue(order3)
        queue.print_info()

        queue.enqueue(order4)
        queue.print_info()

        # Ver el primer elemento sin eliminarlo
        print("Front element: ")
        queue.front().print_info()

        # Eliminar el primer elemento
        queue.dequeue()
        queue.print_info()

        # Obtener el tercer elemento
        nth_element = queue.get_nth(3)
        print("Third element (nth):")
        if nth_element is not None:
            nth_element.print_info()
        else:
            print("No such element.")

if __name__ == "__main__":
    TestQueue.main()
