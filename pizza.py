#Name:Keira Johnson
#Prog Purpose: This program computes the cost of each size pizza
#   Small pizza: $9.99, medium pizza: $12.99, large pizza: $14.99, extra large pizza: $17.99
#   Sales tax rate: 5.5%

import datetime
# define tax rate and prices
SALES_TAX_RATE = .055
PR_S_PIZZA = 9.99
PR_M_PIZZA = 12.99
PR_L_PIZZA = 14.99
PR_X_PIZZA = 17.99

# define global variables
pizzasize = 1 # 1 means small
pizzasize = 2 # 2 means medium
pizzasize = 3 # 3 means large
pizzasize = 4 # 4 means extra large
numpizzas = 0
pizzaprice = 0
subtotal = 0
sales_tax = 0
total = 0
 
############### define program function #################
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to create another order? (Y/N):")
        if yesno.upper() !="Y":
            another_order = False
                    

def get_user_data():
    global pizzasize, numpizzas 
    pizzasize = int(input("Enter a 1 for a small pizza; enter a 2 for a medium pizza; enter a 3 for a large pizza; enter a 4 for a extra large pizza: "))
    numpizzas = int(input("Number of pizzas ordered: "))
        
def perform_calculations():
    global pizzaprice, subtotal, sales_tax, total
    if pizzasize == 1:
        pizzaprice = numpizzas * PR_S_PIZZA
    if pizzasize == 2:
        pizzaprice = numpizzas * PR_M_PIZZA
    if pizzasize == 3:
        pizzaprice = numpizzas * PR_L_PIZZA
    if pizzasize == 4:
        pizzaprice = numpizzas * PR_X_PIZZA

    subtotal = pizzaprice
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    
def display_results():
    print('-------------------------------')
    print('**** PALERMO PIZZA ****')
    print('-------------------------------')
    print('Pizza(s)      x        ' + str(numpizzas)) 
    print('Subtotal      $ ' + format(subtotal,'8,.2f'))
    print('Sales         $ ' + format(sales_tax,'8,.2f'))
    print('Total         $ ' + format(total,'8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))
  
########## call on main program to execute #############
main()    
