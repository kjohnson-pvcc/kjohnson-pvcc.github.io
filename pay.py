#Name:Keira Johnson
#Prog Purpose: This program calculates the pay of each employee

import datetime
# define pay rates and tax rates
HOURLY_PAY_RATE = (16.50, 15.75, 15.75, 19.50)
DEDUCTION_RATES = (.12, .03, .062, .0145)

# define global variables
job = 1 # 1 means Cashier
job = 2 # 2 means Stocker
job = 3 # 3 means Janitor
job = 4 # 4 means Maintenance
numhours = 0
grosspay = ()
fed_tax = 0
state_tax = 0
ss_tax = 0
med_tax = 0
tot_ded = fed_tax + state_tax + ss_tax + med_tax
netpay = 0
 
############### define program function #################
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to input data for another employee? (Y/N):")
        if yesno.upper() !="Y":
            another_employee = False
                    

def get_user_data():
    global job, numhours
    job = int(input("Enter a 1 for Cashier; enter a 2 for Stocker; enter a 3 for Janitor; enter a 4 for Maintenance: "))
    numhours = int(input("Enter the number of hours the employee worked for the week."))
                   
def perform_calculations():
    global grosspay, fed_tax, state_tax, ss_tax, med_tax, HOURLY_PAY_RATE, DEDUCTION_RATES, tot_ded, netpay
    if job == 1:
        grosspay = numhours * HOURLY_PAY_RATE[0]
        
    if job == 2:
        grosspay = numhours * HOURLY_PAY_RATE[1]
        
    if job == 3:
        grosspay = numhours * HOURLY_PAY_RATE[2]
        
    if job == 4:
        grosspay = numhours * HOURLY_PAY_RATE[3]

        fed_tax = grosspay * DEDUCTION_RATES[0]
        state_tax = grosspay * DEDUCTION_RATES[1]
        ss_tax = grosspay * DEDUCTION_RATES[2]
        med_tax = grosspay * DEDUCTION_RATES[3]
        tot_ded = fed_tax + state_tax + ss_tax + med_tax
        netpay = grosspay - tot_ded
    
def display_results():
    print('------------------------------------------')
    print('********* FRESH FOOD MARKETPLACE *********')
    print('------------------------------------------')
    print('Date Range                                ')
    print('Employee Name                             ')
    print('Num Hours Worked               ' + str(numhours)) 
    print('Gross Pay             $ ' + format(grosspay,'8,.2f'))
    print('Federal Income Tax    $ ' + format(DEDUCTION_RATES[0]*grosspay,'8,.2f'))
    print('State Income Tax      $ ' + format(DEDUCTION_RATES[1]*grosspay,'8,.2f'))
    print('Social Security Tax   $ ' + format(DEDUCTION_RATES[2]*grosspay,'8,.2f'))
    print('Medicare Tax          $ ' + format(DEDUCTION_RATES[3]*grosspay,'8,.2f'))
    print('Total Deductions      $ ' + format(fed_tax + state_tax + ss_tax + med_tax,'8,.2f'))
    print('------------------------------------------')
    print('Net Pay               $ ' + format(grosspay - tot_ded,'8,.2f'))
    print(str(datetime.datetime.now()))
 
########## call on main program to execute #############
main()    
