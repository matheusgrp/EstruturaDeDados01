from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        # Se for abertura
        if char in "([{":
            pilha.push(char)

        # Se for fechamento
        elif char in ")]}":
            if pilha.is_empty():
                return False

            topo = pilha.pop()

            if topo != pares[char]:
                return False

    return pilha.is_empty()


# Testes
print(is_balanced("[{}(2+2)]{}")) # True
print(is_balanced("[{}(2+2))]{}")) # False
print(is_balanced("[{}])")) # False

print(" ")
print(is_balanced(""))                         
print(is_balanced("()"))                       
print(is_balanced("({[]})"))                   
print(is_balanced("{[()()]()}"))               
print(is_balanced("if (a[0] > b) { return c; }"))

print(" ")
print(is_balanced("("))                        
print(is_balanced("]"))                        
print(is_balanced("({[)]}"))                   
print(is_balanced("{[(()]}"))                  
print(is_balanced("((()))]"))                  