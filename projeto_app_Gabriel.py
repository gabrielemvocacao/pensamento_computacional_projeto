'''
CRUD


Hamburguer


print('Ola Mundo! - Quebrei essa maldição') #O print exibe na tela


input('Pressione enter para sair') #O input serve para pedir da tela



'''


#  print('\nHamburgueria\n')
# # print('1.cadastro') # Cadastro e login
# print('1. Cardapio')
# print('2. Delivery')
# print('0. Sair')


# while True:

#     escolha_menu = input('\nEscolha uma opção:')

#     if escolha_menu == '1' :

#         print('carregando cardapio...')
#         lanches_disponiveis = input('\nSelecione seu lanche\n 1. Combo carne\n 2. Combo coca\n 3. Combo suco\n \nEscolha uma opção:\n')
#        # print('/n1. Combo carne/n')
#         selecione_os_acompanhamentos = input('\nEscolha até 2 acompanhamentos\n 1. Nuggets\n 2. Batata extra\n 3. Molho Barbecue\n 4. Não quero acompanhamentos\n Selecione um acompanhamento: \n')
#         # Deve selecionar os lanches e acompanhamentos.
#         selecione_os_acompanhamentos = input('\nEscolha o segundo acompanhamento\n 1. Nuggets\n 2. Batata extra\n 3. Molho Barbecue\n 4. Não quero acompanhamentos\nSelecione um acompanhamento: \n')
#         print('\n Finalizando pedido...\n')
#         break

#     elif escolha_menu =='2':
#      print('=== BEM VINDO AO DELIVERY ===')
     
#      print('\nCasa ou Apartamento\n')
     
#     Tipo_moradia = input('Digite Casa ou Apartamento: ').lower()

# # ==== CASA ====
# if Tipo_moradia == 'casa':
#     endereco = input('\nDigite o endereço: ')
#     numero = input('Digite o número: ')
#     referencia = input('Ponto de referência (opcional): ')

# # ==== APARTAMENTO ====
# elif Tipo_moradia == 'apartamento':
#     endereco = input('\nDigite o endereço: ')
#     bloco = input('Digite o bloco: ')
#     morador = input('Nome do morador: ')

# else:
#     print('Opção inválida.')
#     break
    
    
import random
# serve para importar numeros aleatorios

# esse sistema serve para o cliente fazer o pedido, ver o cardapio, se deseja fazer delivey ou não, e para os interessados as vagas
# inserir seus dados (idade e experiencia) para verificar se seus dados são compativeis com o que a vaga pede
clientes = {}
# area dos clientes

combos = {
    '1': ('Combo Classico Burger + Batata + Bebida', 28.90),
    '2': ('Combo Bacon Burger + Batata + Bebida', 32.90),
    '3': ('Combo Chicken Crispy + Batata + Bebida', 33.90),
    '4': ('Combo Cheeseburger Duplo + Batata + Bebida', 34.90)
}
# variavel que funciona pelo codigo inteiro e mostra os combos quando usado

lanches = {
    '5': ('Hamburguer Classico', 17.90),
    '6': ('Bacon Burger', 21.90),
    '7': ('Chicken Crispy Burger', 20.90),
    '8': ('Veggie Burger', 19.90),
    '9': ('Cheeseburger Duplo', 23.90)
}
# variavel que funciona pelo codigo inteiro e mostra os lanches unicos quando usado

acompanhamentos = {
    '1': ('Nuggets', 9),
    '2': ('Batata extra', 7),
    '3': ('Onion Rings', 8),
    '4': ('Molho Barbecue', 4),
    '5': ('Molho Alho', 4),
    '6': ('Molho Especial', 5)
}
# variavel que funciona pelo codigo inteiro e mostra os acompanhamentos quando colocado

sucos = {
    '1': 'Laranja',
    '2': 'Morango',
    '3': 'Maracuja',
    '4': 'Abacaxi'
}
# variavel que funciona pelo codigo inteiro e mostra os sabores dos sucos quando colocado

refrigerantes = {
    '1': 'Coca Cola',
    '2': 'Guarana',
    '3': 'Fanta',
    '4': 'Sprite'
}
# variavel que funciona pelo codigo inteiro e mostra os sabores de refrigerantes quando usado

vagas = {
    '1': ('Cozinheiro', 25, 5),
    '2': ('Atendente', 17, 1),
    '3': ('Chapeiro', 21, 2),
    '4': ('Entregador', 18, 0),
    '5': ('Gerente', 30, 5),
    '6': ('Auxiliar de Cozinha', 18, 0),
    '7': ('Caixa', 18, 1)
}
# variavel que funciona pelo codigo inteiro e mostra as vagas quando usado


def sugestao_chef():
    # função que funciona apenas no local dentro desse (def)

    item = random.choice(list(lanches.values()))

    print('\n⭐ Sugestao do chef')
    print(item[0], 'R$', item[1])
    #  o sisetma mostra um lanche aleaorio com o valor certo do lanche

    resp = input('Deseja adicionar ao pedido? (s/n): ').lower()
    # da a opção do cliente responder se deseja adicionar ao pedido 

    if resp == 's':
        return [(item[0], item[1], 1, 'sugestao')]
    # a resposta sendo s (sim) ele adiciona ao pedido contabilizando o preço e retorna a escolha do pedido

    return []


def escolher_lanches():
    # função que funciona apenas no local dentro desse (def)

    carrinho = []
    total_parcial = 0

    while True:

        print('\nCARDAPIO\n')
        # mostra as opções de pedido 

        for c in combos:

            if c == '3':
                print(c, '-', combos[c][0], '🥇', 'R$', combos[c][1])
            else:
                print(c, '-', combos[c][0], 'R$', combos[c][1])

        for l in lanches:

            if l == '5':
                print(l, '-', lanches[l][0], '🥈', 'R$', lanches[l][1])

            elif l == '9':
                print(l, '-', lanches[l][0], '🥉', 'R$', lanches[l][1])

            else:
                print(l, '-', lanches[l][0], 'R$', lanches[l][1])

        escolha = input('\nEscolha o numero do item: ')
        # da ao cliente a opção de inserir uma resposta

        if escolha in combos:
            item = combos[escolha]

        elif escolha in lanches:
            item = lanches[escolha]

        else:
            print('Opção Inexistente, Tente Novamente.')
            continue
        # caso o cliente escolha alguma opção fora do permitido, esse codigo sinaliza que a opção esta incorreta e o direciona para
        # inserir novamente uma opção correta

        while True:

            try:
                qtd = int(input('Quantidade: '))
                if qtd > 0:
                    # se a opção for menor ou igual a 0 ele sinaliza para o cliente opção invalida e o direciona para inserir novamente
                    # uma opção correta
                    break
                # da ao cliente a escolha da quantidade do pedido
                else:
                    print('Digite uma quantidade válida.')
            except:
                print('Digite apenas números.')
                # exige que as respostas sejam apenas numeros sem letras ou outros caracteres

        carrinho.append((item[0], item[1], qtd, escolha))

        subtotal = item[1] * qtd
        total_parcial += subtotal

        print('\nSubtotal deste item: R$', format(subtotal, '.2f'))
        print('Total parcial do carrinho: R$', format(total_parcial, '.2f'))

        mais = input('\nDeseja adicionar mais lanches? (s/n): ').lower()
        # da ao cliente a opção de inserir uma resposta e se ele deseja adicionar mais lanches

        if mais != 's':
            # se o sistema receber s (sim) retrona para o carrinho
            break

    return carrinho


def escolher_acompanhamentos():
    # função que funciona apenas no local dentro desse (def)

    lista = []

    escolha = input('\nDeseja acompanhamentos? (s/n): ').lower()
    # da ao cliente a opção de inserir uma resposta e se ele deseja acompanhamentos

    if escolha == 's':
        # se o sistema receber s (sim) o direciona para a area de acompanhamentos onde ele pode ver o preço e se deseja realmente
        # adicionar acompanhamentos

        print('\nACOMPANHAMENTOS')

        for a in acompanhamentos:
            print(a, '-', acompanhamentos[a][0], 'R$', acompanhamentos[a][1])
            # mostra ao cliente os acompanhamentos e os preços

        while True:

            ac = input('Escolha um acompanhamento (0 para parar): ')
            # repete a opção de inserir uma resposta ate o sistema receber 0

            if ac == '0':
                break
            # quano sistema receber 0 ele para de repetir

            if ac in acompanhamentos:
                lista.append(acompanhamentos[ac])
            else:
                print('Opção Inexistente, Tente Novamente.')
                # caso o cliente insira uma opção não existente ele o sinaliza isso e o direciona para colocar uma
                # opção correta

    return lista
# apos isso retorna a lista


def escolher_bebida(combo=False):
    # função que funciona apenas no local dentro desse (def)

    while True:

        escolha = input(
            '\nEscolha sua bebida\n'
            '1 Suco\n'
            '2 Refrigerante\n'
            'Escolha: '
        )
        # da ao cliente a opção de inserir uma resposta

        if escolha == '1':
            # se o sistema receber 1 (sucos) mostra ao cliente os sabores disponiveis de sucos

            print('\nSabores de Suco')

            for s in sucos:
                if combo:
                    print(s, '-', sucos[s])
                    # se antes ele tiver escolhido combo não mostra o preço do suco
                else:
                    print(s, '-', sucos[s], 'R$ 9')
                    # caso contrario ele sinaliza o preço do suco ao cliente

            sabor = input('Escolha o suco: ')
            # da ao cliente a opção de inserir uma resposta

            if sabor in sucos:
                return (sucos[sabor], 0 if combo else 9)

        elif escolha == '2':
            # caso o sitema  2 (refrigerantes) ele mostra ao cliente os sabores disponiveis de refrigerantes

            print('\nRefrigerantes')

            for r in refrigerantes:
                if combo:
                    print(r, '-', refrigerantes[r])
                    # se antes ele tiver escolhido combo não mostra o preço do refrigerante
                else:
                    print(r, '-', refrigerantes[r], 'R$ 7')
                    # caso contrario ele sinaliza o preço do refrigerante ao cliente

            refri = input('Escolha o refrigerante: ')
            # da ao cliente a opção de inserir uma resposta

            if refri in refrigerantes:
                return (refrigerantes[refri], 0 if combo else 7)

        else:
            print('Opção Inexistente, Tente Novamente.')
            # caso o cliente insira uma opção não existente ele o sinaliza isso e o direciona para colocar uma
            # opção correta


def escolher_pagamento():
    # função que funciona apenas no local dentro desse (def)

    while True:

        escolha = input(
            '\nForma de pagamento\n'
            '1 Dinheiro\n'
            '2 Cartao\n'
            '3 Pix\n'
            'Escolha: '
        )# da ao cliente a opção de inserir uma resposta

        if escolha == '1':
            return 'Dinheiro'
        # se o sistema receber 1 (dinheiro) permite o cliente a pagar em dinheiro

        elif escolha == '2':
            # se o sistema receber 2 (cartão) da a opção de pagar no credito ou debito

            while True:

                cartao = input(
                    '\nTipo de cartao\n'
                    '1 Credito\n'
                    '2 Debito\n'
                    'Escolha: '
                )

                if cartao == '1':
                    return 'Cartao - Credito'

                elif cartao == '2':
                    return 'Cartao - Debito'

                else:
                    print('Opção Inexistente, Tente Novamente.')
                    # caso o cliente escolha alguma opção fora do permitido, esse codigo sinaliza que a opção esta incorreta 
                    # e o direciona para inserir novamente uma opção correta

        elif escolha == '3':
            return 'Pix'
            # se o sistema receber 3 (Pix) permite o cliente a pagar no pix
        else:
            print('Opção Inexistente, Tente Novamente.')
            # caso o cliente escolha alguma opção fora do permitido, esse codigo sinaliza que a opção esta incorreta 
            # e o direciona para inserir novamente uma opção correta


def fazer_pedido(delivery=False):
     # função que funciona apenas no local dentro desse (def)

    endereco = ''

    if delivery:
        

        print('\nDELIVERY')

        tipo = input('Casa ou Apartamento: ').lower()
        # da a opção do cliente escolher casa ou apartamento 

        if tipo == 'casa':
            # se o cliente inserir casa ou C
            rua = input('Endereco: ')
            numero = input('Numero: ')
            endereco = rua + ', ' + numero

        elif tipo == 'apartamento':
            rua = input('Endereco: ')
            bloco = input('Bloco: ')
            endereco = rua + ', Bloco ' + bloco

    cliente = input('\nDigite seu nome: ')

    if cliente not in clientes:
        clientes[cliente] = {"pedidos": 0}

    print('Pedidos anteriores:', clientes[cliente]["pedidos"])

    clientes[cliente]["pedidos"] += 1

    lanches_escolhidos = sugestao_chef()

    lanches_escolhidos = escolher_lanches()

    acompanhamentos_escolhidos = escolher_acompanhamentos()

    tem_combo = any(item[3] in combos for item in lanches_escolhidos)

    bebida = ('Sem bebida', 0)

    if tem_combo:

        print('\nSeu combo inclui bebida.')
        bebida = escolher_bebida(True)

    else:

        resp = input('\nDeseja adicionar bebida? (s/n): ').lower()

        if resp == 's':
            bebida = escolher_bebida(False)

    pagamento = escolher_pagamento()

    total = 0

    for l in lanches_escolhidos:
        total += l[1] * l[2]

    for a in acompanhamentos_escolhidos:
        total += a[1]

    total += bebida[1]

    taxa_entrega = 0

    if delivery:

        if total >= 60:
            print('\nFrete GRATIS!')
        else:
            taxa_entrega = 10
            print('\nTaxa de entrega: R$10')

    total += taxa_entrega

    numero_pedido = random.randint(1000, 9999)

    tempo = random.randint(20, 40,)

    print('\n' + '='*50)
    print('RESUMO DO PEDIDO')
    print('='*50)

    print('Cliente:', cliente)
    print('Pedido:', numero_pedido)

    if delivery:
        print('Endereco:', endereco)

    print('\nLanches:')

    for l in lanches_escolhidos:
        print(f"- {l[0]} | Quantidade: {l[2]} | R$ {l[1]*l[2]:.2f}")

    if acompanhamentos_escolhidos:

        print('\nAcompanhamentos:')

        for a in acompanhamentos_escolhidos:
            print('-', a[0], 'R$', a[1])

    if bebida[0] != 'Sem bebida':
        print('\nBebida:', bebida[0], 'R$', bebida[1])

    if delivery:
        print('Entrega:', 'Gratis' if taxa_entrega == 0 else 'R$10')

    print('\nPagamento:', pagamento)

    print('\nTotal: R$', format(total, '.2f'))

    print('Tempo estimado:', tempo, 'minutos')

    print('='*50)


while True:

    print('\nMENU PRINCIPAL')
    print('-'*40)
    print('1 Fazer Pedido')
    print('2 Delivery')
    print('3 Trabalhe Conosco')
    print('0 Sair')
    print('-'*40)

    opcao = input('Escolha: ')

    if opcao == '1':
        fazer_pedido(False)

    elif opcao == '2':
        fazer_pedido(True)

    elif opcao == '3':

        print('\nVagas disponiveis')

        for v in vagas:
            print(v, '-', vagas[v][0])

        escolha = input('Escolha a vaga: ')

        if escolha in vagas:

            idade = int(input('Idade: '))
            exp = int(input('Experiencia (anos): '))

            nome, idade_min, exp_min = vagas[escolha]

            if idade >= idade_min and exp >= exp_min:
                print('Perfil aprovado para', nome)
            else:
                print('Requisitos nao atendidos.')

        else:
            print('Vaga invalida.')

    elif opcao == '0':
        print('Encerrando sistema...')
        break

    else:
        print('Opção Inexistente, Tente Novamente.')
