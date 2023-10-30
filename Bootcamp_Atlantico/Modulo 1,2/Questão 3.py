def segundo_maior(lista):
    if len(lista) < 2:
        return "A lista não possui pelo menos dois elementos."

    # Classificar a lista em ordem decrescente
    lista_ordenada = sorted(lista, reverse=True)

    # O segundo maior valor estará na posição 1 da lista classificada
    segundo_maior_valor = lista_ordenada[1]

    return segundo_maior_valor

# Exemplo de uso
input_str = input("Digite uma lista de números separados por espaço: ")
lista_de_numeros = [int(x) for x in input_str.split()]
segundo_maior = segundo_maior(lista_de_numeros)
print("O segundo maior valor na lista é:", segundo_maior)
