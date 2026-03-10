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
# ('Digite a sua escolha')

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

clientes = {}

combos = {
    '1': ('Combo Classico Burger + Batata', 28.90),
    '2': ('Combo Bacon Burger + Batata', 32.90),
    '3': ('Combo Chicken Crispy + Batata', 33.90),
    '4': ('Combo Cheeseburger Duplo + Batata', 34.90)
}

lanches = {
    '5': ('Hamburguer Classico', 17.90),
    '6': ('Bacon Burger', 21.90),
    '7': ('Chicken Crispy Burger', 20.90),
    '8': ('Veggie Burger', 19.90),
    '9': ('Cheeseburger Duplo', 23.90)
}

acompanhamentos = {
    '1': ('Nuggets', 9),
    '2': ('Batata extra', 7),
    '3': ('Onion Rings', 8),
    '4': ('Molho Barbecue', 4),
    '5': ('Molho Alho', 4),
    '6': ('Molho Especial', 5)
}

sucos = {
    '1': 'Laranja',
    '2': 'Morango',
    '3': 'Maracuja',
    '4': 'Abacaxi'
}

refrigerantes = {
    '1': 'Coca Cola',
    '2': 'Guarana',
    '3': 'Fanta',
    '4': 'Sprite'
}

vagas = {
    '1': ('Cozinheiro', 25, 5),
    '2': ('Atendente', 17, 1),
    '3': ('Chapeiro', 21, 2),
    '4': ('Entregador', 18, 0),
    '5': ('Gerente', 30, 5),
    '6': ('Auxiliar de Cozinha', 18, 0),
    '7': ('Caixa', 18, 1)
}


def sugestao_chef():

    item = random.choice(list(lanches.values()))

    print('\n⭐ Sugestao do chef')
    print(item[0], 'R$', item[1])

    resp = input('Deseja adicionar ao pedido? (s/n): ').lower()

    if resp == 's':
        return [(item[0], item[1], 1, 'sugestao')]

    return []


def escolher_lanches():

    carrinho = []
    total_parcial = 0

    while True:

        print('\nCARDAPIO\n')

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

        if escolha in combos:
            item = combos[escolha]

        elif escolha in lanches:
            item = lanches[escolha]

        else:
            print('Opcao invalida.')
            continue

        while True:

            try:
                qtd = int(input('Quantidade: '))
                if qtd > 0:
                    break
                else:
                    print('Digite uma quantidade válida.')
            except:
                print('Digite apenas números.')

        carrinho.append((item[0], item[1], qtd, escolha))

        subtotal = item[1] * qtd
        total_parcial += subtotal

        print('\nSubtotal deste item: R$', format(subtotal, '.2f'))
        print('Total parcial do carrinho: R$', format(total_parcial, '.2f'))

        mais = input('\nDeseja adicionar mais lanches? (s/n): ').lower()

        if mais != 's':
            break

    return carrinho


def escolher_acompanhamentos():

    lista = []

    escolha = input('\nDeseja acompanhamentos? (s/n): ').lower()

    if escolha == 's':

        print('\nACOMPANHAMENTOS')

        for a in acompanhamentos:
            print(a, '-', acompanhamentos[a][0], 'R$', acompanhamentos[a][1])

        while True:

            ac = input('Escolha um acompanhamento (0 para parar): ')

            if ac == '0':
                break

            if ac in acompanhamentos:
                lista.append(acompanhamentos[ac])
            else:
                print('Opcao invalida.')

    return lista


def escolher_bebida(combo=False):

    while True:

        escolha = input(
            '\nEscolha sua bebida\n'
            '1 Suco\n'
            '2 Refrigerante\n'
            'Escolha: '
        )

        if escolha == '1':

            print('\nSabores de Suco')

            for s in sucos:
                if combo:
                    print(s, '-', sucos[s])
                else:
                    print(s, '-', sucos[s], 'R$ 9')

            sabor = input('Escolha o suco: ')

            if sabor in sucos:
                return (sucos[sabor], 0 if combo else 9)

        elif escolha == '2':

            print('\nRefrigerantes')

            for r in refrigerantes:
                if combo:
                    print(r, '-', refrigerantes[r])
                else:
                    print(r, '-', refrigerantes[r], 'R$ 7')

            refri = input('Escolha o refrigerante: ')

            if refri in refrigerantes:
                return (refrigerantes[refri], 0 if combo else 7)

        else:
            print('Opcao invalida.')


def escolher_pagamento():

    while True:

        escolha = input(
            '\nForma de pagamento\n'
            '1 Dinheiro\n'
            '2 Cartao\n'
            '3 Pix\n'
            'Escolha: '
        )

        if escolha == '1':
            return 'Dinheiro'

        elif escolha == '2':

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
                    print('Opcao invalida.')

        elif escolha == '3':
            return 'Pix'

        else:
            print('Opcao invalida.')


def fazer_pedido(delivery=False):

    endereco = ''

    if delivery:

        print('\nDELIVERY')

        tipo = input('Casa ou Apartamento: ').lower()

        if tipo == 'casa':
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

    lanches_escolhidos += escolher_lanches()

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

    tempo = random.randint(20, 40)

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
        print('Opcao invalida.')