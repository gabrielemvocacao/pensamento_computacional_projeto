'''
CRUD


Hamburguer


print('Ola Mundo! - Quebrei essa maldição') #O print exibe na tela


input('Pressione enter para sair') #O input serve para pedir da tela



'''


print('\nHamburgueria\n')
# print('1.cadastro') # Cadastro e login
print('1. Cardapio')
print('2. Delivery')
print('0. Sair')


while True:

    escolha_menu = input('\nEscolha uma opção:')

    if escolha_menu == '1' :

        print('carregando cardapio...')
        lanches_disponiveis = input('\nSelecione seu lanche\n 1. Combo carne\n 2. Combo coca\n 3. Combo suco\n \nEscolha uma opção:\n')
       # print('/n1. Combo carne/n')
        selecione_os_acompanhamentos = input('\nEscolha até 2 acompanhamentos\n 1. Nuggets\n 2. Batata extra\n 3. Molho Barbecue\n 4. Não quero acompanhamentos\n Selecione um acompanhamento: \n')
        # Deve selecionar os lanches e acompanhamentos.
        selecione_os_acompanhamentos = input('\nEscolha o segundo acompanhamento\n 1. Nuggets\n 2. Batata extra\n 3. Molho Barbecue\n 4. Não quero acompanhamentos\nSelecione um acompanhamento: \n')
        print('\n Finalizando pedido...\n')

        print('\n ==Delivery== \n')

        entrega = input('\nDigite seu endereço:\n')
        print('1. Casa')
        print('2. Apartamento')       
        Casa_ou_apartamento = input('\nCasa ou Ap:')

    elif Casa_ou_apartamento == '1': input('Numero da residencia:')

    elif Casa_ou_apartamento == '2' : input('Numero do apartamento:')
    input ('\nBloco do condominio:\n')

    
    


        


   # elif escolha_menu == '2' :
        
      # entrega = input('\nDigite seu endereço:\n')
      # print('1. Casa')
       #print('2. Apartamento')       
      # Casa_ou_apartamento = input('\nCasa ou Ap:')

    #elif Casa_ou_apartamento == '1': input('Numero da residencia:')

   # elif Casa_ou_apartamento == '2' : input('Numero do apartamento:')
    #input ('\nBloco do condominio:\n')


    

    
        
        


        


    






