RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
calculation=1
RESET = "\033[0m"  # Reset to default color
dollar=f'''
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡾⠧⠀⠀⠥⢀⡀⠀⠀
⠀⠀⠀⢀⣴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠑⡄
⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁
⠀⢀⣻⠁⠀⠀⠀⣰⢿⠀⠸⣽⣗⠖⠃⠀
⠀⠸⢼⠀⠀⠀⠀⣗⢽⠀⠄⠀⠁⠀⠀⠀
⠀⢸⠝⡆⠀⠀⠀⠈⠛⠃⠰⠤⢀⠀⠀⠀
⠀⠀⢯⠜⠦⡀⠀⠀⠀⠀⠀⠀⠀⠉⢂⠀
⠀⠀⠀⠓⢎⣝⠕⣲⡆⠀⡀⠀⠀⠀⠀⠆
⠀⠀⠀⠀⣄⠈⢙⢕⡇⠀⣿⡆⠀⠀⠀⢸
⠀⣠⠔⠉⠈⠑⠴⢬⡇⠀⡷⠃⠀⠀⠀⡈
⠸⡡⢓⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁
⠀⠈⠫⣎⡝⡢⢤⣀⠀⠀⣀⣀⡤⡾⠃⠀
⠀⠀⠀⠀⠉⠚⣔⣿⣤⣤⡽⠓⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠛⠛⠋⠀⠀⠀⠀⠀⠀'''
print(f"\n{YELLOW}{dollar}")
print(f"{RED}Welcome to the Tip Calculator Pro.")
print("Created By Hari Ravendran")

def calculate():
    global calculation
    tot=input(f"{GREEN}What was the total bill? $")
    tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
    num_of_people=input("How many people to split the bill? ")
    try:
        tot = float(tot)
        tip = int(tip)
        num_of_people = int(num_of_people)
    except:
        if isinstance(num_of_people,str) or isinstance(tip,str) or isinstance(tot,str):
            print(f"{RED}Invalid Entry. Please retry.")
    else:
        tot = float(tot)
        tip = int(tip)
        num_of_people = int(num_of_people)
        tipamount=tot*(tip/100)
        tipamount+=tot
        per_person=round(tipamount/num_of_people,2)
        print(f"Each person should pay: $ {per_person}")
        calculation+=1

def ending():
    print(f"\n{YELLOW}Thank you for using Tip Calculator Pro.{RESET}\n")
    input("Press Enter to exit...")


is_on=True
while is_on:
    print(f"\n{YELLOW}Calculation No:{calculation}")
    calculate()
    q=input(f"{RED}Click 'Y' to continue calculating your tip:").lower()
    if q!='y':
        is_on=False
        ending()



