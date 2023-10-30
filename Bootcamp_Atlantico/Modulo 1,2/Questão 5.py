def encontrar_maior_e_menor(lista):
    if not lista:
        return None, None  # Retorne None se a lista estiver vazia

    maior_numero = menor_numero = lista[0]

    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero

    return maior_numero, menor_numero

# Exemplo de uso
lista_de_numeros = input("Digite uma lista de números separados por espaço: ").split()
lista_de_numeros = [int(x) for x in lista_de_numeros]
maior, menor = encontrar_maior_e_menor(lista_de_numeros)
print("O maior número na lista é:", maior)
print("O menor número na lista é:", menor)
