# #Define the Menu of Restaurant.
menu={
    'Pizza':199,
    'Pasta':170,
    'Burger':99,
    'Noodles':180,
    'Salad':80,
    'Cold Coffee':120,
    'Hot Coffee':70,
    'Orange Juice':50,
    }

#Greet
print('Welcome to PYTHON Restaurant')
print( 'Pizza: Rs199\nPasta: Rs170\nBurger: Rs99\nNoodles: Rs180\nSalad: Rs80\nCold Coffee: Rs120\nHot Coffee: Rs70\nOrange Juice: Rs50')
order_total=0
#99+80=179

item_1=input('Enter the name of item you want to order=')
if item_1 in menu:
    order_total +=menu[item_1]
    print(f'Your item {item_1} has been added to your order')

else:
    print(f'ordered item {item_1} is not available yet!')

another_order=input('Do You want to add another item?  (Yes/No)')
if another_order=='Yes':
    item_2=input('Enter the name of Second item=')
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f'Item {item_2} has been added to order')
    else:
        print(f'Ordered Item {item_2} is not available!')
print(f'The Total amount of item is {order_total}  ')


