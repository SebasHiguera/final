states = ["California", "New York", "Texas", "Michigan", "Florida", "Ohio", "Colorado", "Nevada", "Arizona", "Hawaii"]
median_values = [505000, 313000, 172000, 154000, 215000, 145000, 343000, 267000, 225000, 615000]
price_num = 0

def price_to_house(money):
    global states
    global median_values
    for i in range(len(states)):
        if money > median_values[i]:
            print(states[i])

def state_number(user_state):
    global price_num
    if user_state == 'California':
        price_num = 0
    elif user_state == 'New York':
        price_num = 1
    elif user_state == 'Texas':
        price_num = 2
    elif user_state == 'Michigan':
        price_num = 3
    elif user_state == 'Florida':
        price_num = 4
    elif user_state == 'Ohio':
        price_num = 5 
    elif user_state == 'Colorado':
        price_num = 6
    elif user_state == 'Nevada':
        price_num = 7
    elif user_state == 'Arizona':
        price_num = 8
    elif user_state == 'Hawaii':
        price_num = 9
    else:
        print("")

def savings(money,salary):
    years = 0
    saved = money
    while saved < median_values[price_num]:
        saved += salary * .25
        years += 1
    return years





states = ["California", "New York", "Texas", "Michigan", "Florida", "Ohio", "Colorado", "Nevada", "Arizona", "Hawaii"]
median_values = [505000, 313000, 172000, 154000, 215000, 145000, 343000, 267000, 225000, 615000]
price_num = 0

def price_to_house(money):
    global states
    global median_values
    for i in range(len(states)):
        if money > median_values[i]:
            print(states[i])

def state_number(user_state):
    global price_num
    if user_state == 'California':
        price_num = 0
    elif user_state == 'New York':
        price_num = 1
    elif user_state == 'Texas':
        price_num = 2
    elif user_state == 'Michigan':
        price_num = 3
    elif user_state == 'Florida':
        price_num = 4
    elif user_state == 'Ohio':
        price_num = 5 
    elif user_state == 'Colorado':
        price_num = 6
    elif user_state == 'Nevada':
        price_num = 7
    elif user_state == 'Arizona':
        price_num = 8
    elif user_state == 'Hawaii':
        price_num = 9
    else:
        print("")

def savings(money,salary):
    years = 0
    saved = money
    while saved < median_values[price_num]:
        saved += salary * .25
        years += 1
    return years
