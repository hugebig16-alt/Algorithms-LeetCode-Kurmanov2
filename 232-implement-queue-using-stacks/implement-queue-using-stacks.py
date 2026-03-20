class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        # добавляем элемент в входнои стек
        self.in_stack.append(x)

    def pop(self):
        # если выходнои пуст, переливаем элементы
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack.pop()

    def peek(self):
        # аналогично pop, но не удаляем
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack[-1]

    def empty(self):
        # очередь пуста если оба стека пусты
        return not self.in_stack and not self.out_stack