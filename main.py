median_values = [505000, 313000, 172000, 154000, 215000, 145000, 343000, 267000, 225000, 615000]
states = ["California", "New York", "Texas", "Michigan", "Florida", "Ohio", "Colorado", "Nevada", "Arizona", "Hawaii"]

prices = {'California': 505000, 'New York': 313000, 'Texas': 172000, 'Michigan': 154000, 'Florida': 215000, 'Ohio': 145000, 'Colorado': 343000, 'Nevada': 267000, 'Arizona': 225000, 'Hawaii': 615000}


def price_to_house(money):
  for i in range(len(states)):
    if money > median_values[i]:
      print(states[i])

# def state_number(user_state):
#   return states.index(user_state)
#     global price_num
#     if user_state == 'California':
#         price_num = 0
#     elif user_state == 'New York':
#         price_num = 1
#     elif user_state == 'Texas':
#         price_num = 2
#     elif user_state == 'Michigan':
#         price_num = 3
#     elif user_state == 'Florida':
#         price_num = 4
#     elif user_state == 'Ohio':
#         price_num = 5 
#     elif user_state == 'Colorado':
#         price_num = 6
#     elif user_state == 'Nevada':
#         price_num = 7
#     elif user_state == 'Arizona':
#         price_num = 8
#     elif user_state == 'Hawaii':
#         price_num = 9
#     else:
#         print("")

def savings(money,salary):
  years = 0
  while money < prices[user_state]:
    years += 1
    money += salary * .25
  money -= prices[user_state]
  return years, money

if __name__ == "__main__":
  counter = 0
  
  print("###################################")
  print("         Median Home Values\n")
  print("   Arizona:     $225000")
  print("California:     $505000")
  print("  Colorado:     $343000")
  print("   Florida:     $215000")
  print("    Hawaii:     $615000")
  print("  Michigan:     $154000")
  print("    Nevada:     $267000")
  print("  New York:     $313000")
  print("      Ohio:     $145000")
  print("     Texas:     $172000\n")
  print("###################################")

  money = int(input("How much money can you spend on a house? "))
  print(f'\nWith ${money}, you could live in the following states: \n')
  price_to_house(money)
  
  user_state = input("\nRegardless of cost, what state would you like to live in? (write  exactly as written) ")
  if money >= prices[user_state]:
    money -= prices[user_state]
    print(f"\nYou can afford to live here, with ${money} remaining")

  else:
    print(f"\nYou cannot afford to live here, you still need ${prices[user_state] - money}\n") 
    print("It is advised that people save 25% of their salary for a house")
    salary = int(input("What is your yearly salary? "))

    years, money = savings(money, salary)
    print(f"\nWith a yearly salary of ${salary}, it would take about {years} year(s) to save enough money to live in {user_state}")
    print(f"You have ${money} left for another house")
    counter += years

  ask = input("\nWould you like to buy another house? (yes/no) ")
  if ask == 'yes':
    ask = True
  else:
    ask = False
  
  while ask == True:
    user_state = input("\nWhat state would you like to buy another house in? ")
    if money > prices[user_state]:
      money -= prices[user_state]
      print(f"\nYou can afford another house here, with ${money} remaining")
    else:
      print(f"\nYou cannot afford another house here, you still need ${prices[user_state] - money}\n")
      years, money = savings(money, salary)
      print(f"It will take about another {years} year(s) to save enough money to buy another house in {user_state}")
      print(f"You have ${money} left")
      counter += years
  
    ask = input("\nWould you like to buy another house? (yes/no) ")
    if ask == 'yes':
        ask = True
    else:
      ask = False
  
  print(f"It has taken you {counter} years")