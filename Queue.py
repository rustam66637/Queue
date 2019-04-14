class Queue:
    def __init__(self):
        self.queue = []# инициализация хранилища данных

    def enqueue(self, item):
        self.queue.append(item)# вставка в хвост

    def dequeue(self):
        if self.size() == 0:
            return None # если очередь пустая
        else:
            s = self.queue[0]
            del self.queue[0]
            return s# выдача из головы

    def size(self):
        return len(self.queue) # размер очереди
