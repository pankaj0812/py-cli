from cli.data_structues.node import Node
from cli.data_structues.queue import Queue

class BinaryTree:
    def __init__(self):
        self.root = None

    def level_order_insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        queue = Queue()
        queue.enqueue(self.root)

        while queue.get_len():
            node = queue.dequeue()
