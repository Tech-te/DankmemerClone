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

try:
  amount_of_coins = open("coins.txt", "r")
  amount_of_bank_coins = open("bankcoins.txt", "r")
  bank_limit = open("banklimit.txt", "r")
except:
  amount_of_coins = open("coins.txt", "w")
  amount_of_bank_coins = open("bankcoins.txt", "w")
  bank_limit = open("banklimit.txt", "w")
# here are all the variables
x = ""

coins = (amount_of_coins.read())
bank_coins = (amount_of_bank_coins.read())
coins = int(coins)
bank_coins = int(bank_coins)

amount_of_coins.close()
amount_of_bank_coins.close()

def write_coins(x):
  amount_of_coins = open("coins.txt", "w")
  amount_of_coins.write(x)
  amount_of_coins.close()
def write_bank_coins(x):
  amount_of_bank_coins = open("bankcoins.txt", "w")
  amount_of_bank_coins.write((x))
  amount_of_bank_coins.close()
def write_bank_limit(x):
  bank_limit = open("bank_limit.txt", "w")
  bank_limit.write(x)
  bank_limit.close()

def commands():
    print("pls exit - exits program")
    print("pls beg - beg for coins")
    print("pls happyface - :)")
    print("pls battle - wanna risk your life for some money in battle?")
    print("pls dep all - deposits all of your money from your wallet into the bank")
    print("pls bal - shows your balance")
    print("pls banklimit - shows the limit of money the bank can hold")
    print("pls commands - shows all the commands (like right now)")

# welcome!
print("Welcome to Pls do This")
command = input("Would like to see commands (y/n)")
if command == "y":
  commands()
else:
  pass

# the main program

while x != "pls exit":
  bank_coins_limit = bank_limit.read()
  bank_coins_space = int(bank_coins_limit) - bank_coins
  depositable_coins = bank_coins_space
  chance_beg = random.randint(0, 100)
  chance_war = random.randint(0, 100)
  x = input("")
  if x == "pls happyface":
    print(":)")
  elif x == "pls work":
    start_work1 = time.time()
    print("Type the following in the chat (You have a limited time!):")
    work1_sentence = ("I am a sheep and I like pineapples.")
    print(work1_sentence)
    work_input = input("")
    if work_input == work1_sentence:
      if time.time() - start_work1 <= 5:
        print("Good stuff user! Here's some allowance for you.")
      else:
        print("uGGHGH. yOur So SlOW.")
    else:
      print("Your such a dumbo head that you can't even type something corectly. I never want to see that again!")

  elif x == "pls beg":
    if chance_beg > 70:
      random_saying1 = ["Poor doggo, here's something to buy yourself something", "Here little boy, you need some milk.", "There goes my nintedo switch savings"]
      print(random_saying1[random.randint(0,2)])
      beg_coins = random.randint(60, 200)
      coins += beg_coins
      print("We'll need some more bank space...")
      bank_coins_limit += random.randint(0, 50)
    else:
      random_saying2 = ["Me not investing one bit for this mangy doggo", "Lol, no one likes you", "I don't think so buddy"]
      print(random_saying2[random.randint(0,2)])
  elif x == "pls battle":
    input_battle = input("Are you sure you want to battle? There is a big chance you will die! (y/n)")
    if input_battle == "y":
      print("Time to get da spoils of war!")
      if chance_war > 30:
        print("You survived and got da spoils of war")
        war_coins = random.randint(0, 1000)
        coins += war_coins
        print("You got", war_coins,"coins")
        print("You have unlocked more space for your treasure...")
        bank_coins_limit += 100
      else:
        print("𝙔𝙤𝙪 𝙙𝙞𝙚𝙙 and ain't getting any spoils of war")
        coins -= coins
    else:
      print("I guess you're not brave enough!")
  elif x == "pls dep all":
    if (bank_coins_space) < coins:
      if (bank_coins_space) > 0:
        coins -= depositable_coins
        bank_coins += depositable_coins
        depositable_coins -= depositable_coins
        print(depositable_coins, "coins deposited")
      else:
        print("This bank can't stuff any more coins for you.")
    else:
      print(coins, "coins deposited")
      bank_coins += coins
      coins -= coins
  elif x == "pls profile":
    print("This isn't working right now so just ignore this ever happened.")
  elif x == "pls bal":
    print("You have", str(coins), "in your wallet")
    print("You also have", str(bank_coins), "in your bank")
  elif x == "pls banklimit":
    print("Your bank coins limit is", str(bank_coins_limit))
  elif x == "pls exit":
    pass
  elif x == "pls commands":
    commands()
  else:
    print("That is not a command. Pls try again")
  write_bank_limit(str(bank_coins_limit))
  write_bank_coins(str(bank_coins))
  write_coins(str(coins))
  amount_of_coins.close()
  amount_of_bank_coins.close()
  bank_limit.close()

  


    

    
    
