from stack import Stack

class QueueUsingStacks:
    """
    Fila (Queue) implementada usando duas pilhas (Stacks)
    para manter o comportamento FIFO (First In, First Out).
    """
    def __init__(self):
        self.pilha_principal = Stack()   # Onde entra
        self.pilha_aux = Stack()         # Onde sai

    def enqueue(self, data):
       
        self.pilha_principal.push(data)

    def dequeue(self):
       
        if self.pilha_aux.is_empty():
            while not self.pilha_principal.is_empty():
                self.pilha_aux.push(self.pilha_principal.pop())

        
        if self.pilha_aux.is_empty():
            raise Exception("Fila vazia")

        return self.pilha_aux.pop()

    def is_empty(self):
        return self.pilha_principal.is_empty() and self.pilha_aux.is_empty()

    def __str__(self):
        temp_principal = Stack()
        temp_aux = Stack()
        result = []

        while not self.pilha_aux.is_empty():
            val = self.pilha_aux.pop()
            result.append(val)
            temp_aux.push(val)

        while not self.pilha_principal.is_empty():
            val = self.pilha_principal.pop()
            temp_principal.push(val)

        while not temp_principal.is_empty():
            val = temp_principal.pop()
            result.append(val)
            self.pilha_principal.push(val)

        while not temp_aux.is_empty():
            self.pilha_aux.push(temp_aux.pop())

        if not result:
            return "Fila vazia"

        result[0] = f"{result[0]} (Início)"
        result[-1] = f"{result[-1]} (Fim)"
        return "\n↓\n".join(str(x) for x in result)