#Name:Keira Johnson
#Prog Purpose: This program calculates the pay of each employee

import datetime
# define hourly pay rates
HOURLY_PAY_RATES = (16.50, 15.75, 15.75, 19.50)

# define deduction rates
DEDUCTION_RATES = (.12, .03, .062, .0145)

# define global variables
job = 1 # 1 means Cashier 2 means Stocker 3 means Janitor 4 means Maintenance
numhours = 0
grosspay = 0
fed_rate = 0
state_rate = 0
ss_rate = 0
med_rate = 0
tot_ded = 0
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
    global grosspay, fed_rate, state_rate, ss_rate, med_rate, tot_ded, netpay
    if job[0] == 1:
        grosspay = numhours * HOURLY_PAY_RATES
    if job[1] == 2:
        grosspay = numhours * HOURLY_PAY_RATES
    if job[2] == 3:
        grosspay = numhours * HOURLY_PAY_RATES
    if job[3] == 4:
        grosspay = numhours * HOURLY_PAY_RATES

    fed_rate = grosspay * DEDUCTION_RATES
    state_rate = grosspay * DEDUCTION_RATES
    ss_rate = grosspay * DEDUCTION_RATES
    med_rate = grosspay * DEDUCTION_RATES
    tot_ded = fed_rate + state_rate + ss_rate + med_rate
    netpay = grosspay - tot_ded
    
def display_results():
    print('------------------------------------------')
    print('********* FRESH FOOD MARKETPLACE *********')
    print('------------------------------------------')
    print('Date Range                                ')
    print('Employee Name                             ')
    print('Num Hours Worked        ' + str(numhours)) 
    print('Gross Pay             $ ' + format(grosspay,'8,.2f'))
    print('Federal Income Tax    $ ' + format(fed_rate,'8,.2f'))
    print('State Income Tax      $ ' + format(state_rate,'8,.2f'))
    print('Social Security Tax   $ ' + format(ss_rate,'8,.2f'))
    print('Medicare Tax          $ ' + format(med_rate,'8,.2f'))
    print('Total Deductions      $ ' + format(tot_ded,'8,.2f'))
    print('------------------------------------------')
    print('Net Pay               $ ' + format(netpay,'8,.2f'))
    print(str(datetime.datetime.now()))
  
########## call on main program to execute #############
main()    
