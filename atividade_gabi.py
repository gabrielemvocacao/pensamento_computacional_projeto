'''
CRUD


Hamburger

print('Ola Mundo! - Quebrei essa maldição') #O print exibe na tela


input('Pressione Enter para sair') #O input serve para pedir da tela
'''
print('\nHamburgueria\n')

print ('1. Cardapio')
print ('2. Delivery')
print ('0. Sair')
print ('\nEscolha uma opção!\n')

while True:

    escolha_menu = input ('\n Escolha uma opção: ')

    

  Lanches_Disponiveis = input ('\nSelecione seu lanche\n 1. Combo Carne\n 2. Combo Coca\n 3. Combo Suco\n Escolha uma opção:')
       
    selecione_os_acompanhamentos = input('\nEscolha até 2 acompanhamentos\n 1. Nuggets\n 2. Batata Extra\n 3. Molho Barbecue\n 4. Batata Com Cheddar\n 0. Não quero acompanhamentos\n Escolha uma opção:')

    selecione_os_acompanhamentos = input('\nEscolha até 2 acompanhamentos\n 1. Nuggets\n 2. Batata Extra\n 3. Molho Barbecue\n 4. Batata Com Cheddar\n 0. Não quero acompanhamentos\n Escolha uma opção:')
        
     print ('\nFinalizando pedido...')

    print ('\nPedido finalizado com sucesso')
    break
    
    if escolha_menu == '2' :
        
        entrega = input ('\nDigite seu endereço:\n')
        numero_residencia = input ('\nCasa ou Apartamento\n')