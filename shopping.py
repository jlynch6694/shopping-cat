my_list = {}

def shopping_list(quant, prod):
    my_list[prod]= quant

def print_list():
    print('\n\n\n')
    for p,q in my_list.items():
        print('{}: {}'.format(p,q))
while True:
    print(my_list)
    print('Write quit at any time to stop shopping! ')
    prod=input('What would you like to purchase, my dear? ')
    quant=input('How much of this would you like to puchase, my dear? ')
    if prod == 'quit' and quant == 'quit':
        print_list()
        break
    elif prod =='remove item' and quant =='remove item':
        remover=input('What would you like to remove, my dear? ')
        del my_list[remover]
    else:
        my_list[prod]=quant
