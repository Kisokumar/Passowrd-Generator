import secrets
import string 
import time
import sys
import os

alphabet = string.ascii_letters + string.digits + string.punctuation  

def cls():
    os.system('cls' if os.name=='nt' else 'clear') 

def typer(string,timer=(0.01),remove="no"):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(timer)
    if remove=="yes":
        cls()

def passwordgenerator():
    cls()
    many = int(input(f'''
    -----------------------------------------------------------------
    --------------------------Password Generator---------------------
    -----------------------------------------------------------------
    
    How many passwords would you like? : '''))
    time.sleep(0.5)
    cls()
    rand = int(input(f'''
    -----------------------------------------------------------------
    --------------------------Password Generator---------------------
    -----------------------------------------------------------------

    How many characters should the passwords be? : '''))
    cls()
    print('\n\nWorking . . .')
    time.sleep(1)
    cls()
    alphabet = string.ascii_letters + string.digits + string.punctuation 
    y=0
    for x in range(many): 
        y+=1
        password = "".join(secrets.choice(alphabet) for i in range(rand)) 
        temp = f'''Password # {y} - - -> {password}\n'''
        typer(temp)
        time.sleep(0.1)
    #region
    print("\n\n\n\nDone!\n\nYou have 60 seconds to save passwords with either a screenshot or the clipboard! \n\n\n\n")
    time.sleep(60)
    cls()
    print("I will now exit automatically!")
    for i in range(3):
        time.sleep(1)
        print(f"{i} !")
        cls()
    print("Goodbye!")
    time.sleep(3)
    cls()
    exit()
    #endregion

if __name__=="__main__":
    passwordgenerator()
