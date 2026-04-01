from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        """
        Função para empilhar na pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        main_stack.push(data)

        # Se min_stack estiver vazia ou o novo valor for menor ou igual ao topo
        if min_stack.is_empty() or data <= min_stack.items[-1]:
            min_stack.push(data)


    def pop_aux():
        """
        Função para desempilhar da pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        if main_stack.is_empty():
            return None

        valor = main_stack.pop()

        # Se o valor removido é o mínimo atual, remove da min_stack também
        if valor == min_stack.items[-1]:
            min_stack.pop()

        return valor


    def get_min():
        """
        Função para retornar o mínimo atual.
        """
        if min_stack.is_empty():
            raise IndexError("Pilha vazia")

        return min_stack.items[-1]


    # Testes
    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")