def ordenar_por_nome(lista_de_pessoas):
    # Use a função sorted com uma chave personalizada para ordenar a lista por nome
    lista_ordenada = sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0])
    return lista_ordenada

# Exemplo de uso
lista_de_pessoas = input("Digite uma lista de pessoas (nome, idade, altura) separadas por espaço: ").split()
lista_ordenada = ordenar_por_nome(lista_de_pessoas)
print(lista_ordenada)
