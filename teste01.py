class Node:
    def __init__(self, data):
        self.data = data      # Valor do nó
        self.next = None      # Ponteiro para o próximo nó


class SingleLinkedList:
    def __init__(self):
        self.head = None      # Ponteiro para o início da lista
        self.tail = None      # Ponteiro para o final da lista
        self.size = 0         # Tamanho da lista

    def append(self, data):
        new_node = Node(data)

        if self.head is None:  # lista vazia
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Índice fora do limite")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if self.size == 0:
                self.tail = new_node

        elif index == self.size:
            self.append(data)
            return

        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next

            new_node.next = prev.next
            prev.next = new_node

        self.size += 1

    def __str__(self):
        elements = []
        trav = self.head
        while trav:
            elements.append(str(trav.data))
            trav = trav.next
        return " -> ".join(elements)


# Teste
linked_list = SingleLinkedList()
linked_list.append(5)
linked_list.append(23)
linked_list.append(7)
linked_list.append(13)

print("Lista original:")
print(linked_list)

linked_list.insert(2, 11)

print("\nLista após inserir 11 na terceira posição:")
print(linked_list)