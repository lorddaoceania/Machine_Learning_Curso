def elementos_exclusivos(lista1, lista2):
    exclusivos = []
    
    # Verifica os elementos exclusivos da lista1
    for elemento in lista1:
        if elemento not in lista2:
            exclusivos.append(elemento)
    
    # Verifica os elementos exclusivos da lista2
    for elemento in lista2:
        if elemento not in lista1:
            exclusivos.append(elemento)
    
    return exclusivos

# Exemplo de uso
lista1 = input("Digite os elementos da lista 1: ").split()
lista2 = input("Digite os elementos da lista 2: ").split()
resultado = elementos_exclusivos(lista1, lista2)
print(resultado)
