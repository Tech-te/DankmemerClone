# imports modules
import random, sys, time

# making print() cooler
def pause(x):
    time.sleep(x)

def print2(x):
  for i in range(len(x)):
      print(x[i], end ="")
      pause(0.04)
      sys.stdout.flush()
  print("")

def input_print(x):
  for i in range(len(x)):
      print(x[i], end ="")
      pause(0.04)
      sys.stdout.flush()

# here are all the variables
x = ""
coins = 0
bank_coins = 0
bank_coins_limit = 1000
bank_coins_space = bank_coins_limit - bank_coins
depositable_coins = bank_coins_space
amount_of_coins = open("coins.txt", "w")
amount_of_coins.close()
amount_of_bank_coins = open("bankcoins.txt", "w")
amount_of_bank_coins.close()
def add_coins(x):
  amount_of_coins = open("coins.txt", "r")
  added_thing2 = str(eval(str(x) + (amount_of_coins.read())))
  amount_of_coins = open("coins.txt", "a")
  amount_of_coins.write(added_thing2)
  amount_of_coins.close()
def add_bank_coins(x):
  amount_of_bank_coins = open("bankcoins.txt", "r")
  added_thing = str(eval(str(x) + (amount_of_bank_coins.read())))
  amount_of_bank_coins = open("bankcoins.txt", "a")
  amount_of_bank_coins.write((added_thing))
  amount_of_bank_coins.close()


# welcome!
print("Welcome to Pls do This")
print("Type pls (command) to do a command")
command = input("Would like to see commands (y/n)")
if command == "y":
  def commands():
    print("pls exit - exits program")
    print("pls beg - beg for coins")
    print("pls happyface - :)")
    print("pls battle - wanna risk your life for some money in battle?")
    print("pls dep all - deposits all of your money from your wallet into the bank")
    print("pls bal - shows your balance")
    print("pls banklimit - shows the limit of money the bank can hold")
    print("pls commands - shows all the commands (like right now)")
  commands()
else:
  pass

# the main program
while x != "pls exit":
  chance_beg = random.randint(0, 100)
  chance_war = random.randint(0, 100)
  x = input("")
  if x == "pls happyface":
    print(":)")
  elif x == "pls beg":
    if chance_beg > 50:
      print("Poor doggo, here's something to buy yourself something")
      beg_coins = random.randint(60, 200)
      coins += beg_coins
      add_coins(beg_coins)
    else:
      print("Me not investing one bit for this mangy doggo")
  elif x == "pls battle":
    print("Time to get da spoils of war!")
    if chance_war > 50:
      print("You survived and got da spoils of war")
      war_coins = random.randint(0, 1000)
      coins += war_coins
      add_coins(war_coins)
    else:
      print("𝙔𝙤𝙪 𝙙𝙞𝙚𝙙 and ain't getting any spoils of war")
      coins -= coins
      add_coins(-coins)
  elif x == "pls dep all":
    print("Depositing all.")
    if (bank_coins_limit - coins) < 0:
      if (bank_coins_space) > 0:
        coins -= depositable_coins
        bank_coins += depositable_coins
        depositable_coins -= depositable_coins
        add_coins(-depositable_coins)
        add_bank_coins(depositable_coins)
      else:
        print("This bank can't stuff any more cash for you.")
    else:
      bank_coins += coins
      coins -= coins
      add_bank_coins(coins)
      add_coins(-coins)
  elif x == "pls bal":
    print("You have", coins, "in your wallet")
    print("You also have", bank_coins, "in your bank")
  elif x == "pls banklimit":
    print("Your bank coins limit is", bank_coins_limit)
  elif x == "pls exit":
    pass
  elif x == "pls command":
    commands()
  else:
    print("That is not a command. Pls try again")


    

    
    
