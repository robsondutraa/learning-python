produtos = ('Shampoo', 10.50,
            'Geladeira', 299.30,
            'Armário', 430.23,
            'Macarrão', 17.30,
            'Feijão', 8.90,
            'Arroz', 5.50,)
print('-=-'*13)
print(f'{"LISTAGEM DE PRODUTOS":^13}')                  # Este laço for percorre a lista 'produtos' usando índices numéricos.
                                                        # A função range(0, len(produtos)) cria uma sequência de números de 0 até o último índice da lista.
                                                        # A variável 'posição' recebe cada um desses índices em cada iteração.
                                                        # Isso permite acessar o elemento correspondente da lista com produtos[posição].
print('-=-'*13)
for posição in range(0, len(produtos)):
    if posição % 2 == 0:
        print()
        print(f'{produtos[posição]:.<30}', end=' ')
    else:
        print(f'R${produtos[posição]:.2f}')
print('-=-'* 13, )

