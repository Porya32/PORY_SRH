import rainbowtext, pyfiglet 
import datetime
from os import system
from time import*
from random import choice, randint
import os,sys,time
from colorama import Fore, Back
import random

red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
boldblue='\033[0m'

os.system('clear')
print(f'{Fore.MAGENTA}')
n = 1
r = "="
while (n <= 100):
        print(r,f"%{n}")
        n = n + randint(1,5)
        r = r + "="
        sleep(000000.1)

os.system('clear')

print(f'{Fore.GREEN}')
print(f'{Fore.GREEN}')
print(f'{Fore.GREEN}')

x = str(datetime.datetime.now())
print("  started \033[93m " + (x))
x = ("""\033[35m
         ⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⣀⠈⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠈⣀⠀⠀⠉⠙⠿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⢶⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⡶⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿
⣿⣿⣿⢁⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣀⡘⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠛⣉⣉⣉⣏⣙⠛⠿⣿⣦⠈⣿⣿⣿⣿⣿⣿⣿⡟⢀⣴⡿⠿⠛⡋⣹⣍⣉⣉⠛⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣧⠹⣿⣿⡟⠁⠔⠉⠁⠀⠀⠀⠀⠈⠐⠀⠙⣷⣼⢸⣿⣿⣿⣿⡇⣧⡾⠉⠀⠊⠁⠀⠀⠀⠀⠈⠙⠢⠈⢻⣿⣿⢏⣽⣿
⣿⣿⠗⠈⠉⠀⠘⠤⠤⣀⣀⠀⡀⠀⠀⠤⠀⢀⣿⣿⢸⣿⣿⣿⣿⡇⣿⣷⡀⠠⠤⣀⡀⢀⡀⡀⡀⠤⠔⠃⢀⠉⠁⠺⢿⣿
⡿⢃⣴⣾⣿⣿⣷⣶⣤⣤⣄⣠⣇⣤⣴⣶⣾⣿⣿⡇⢸⣿⣿⣻⣿⡇⢻⣿⣿⣷⣶⣦⣤⣼⣄⣤⣤⣤⣶⣾⣿⣿⣷⣦⡘⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢸⡟⣿⣿⣿⡇⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⡇⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣠⣾⠀⣸⣿⣿⣿⣿⡇⢸⣦⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⣩⢁⣾⣿⣿⠀⣿⣿⣿⣿⣿⣧⠀⣿⣿⣦⢸⡇⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣻⣿
⣿⣿⡄⠈⢙⠛⠛⠛⢋⣉⣀⣤⣶⣾⣿⡌⣿⡟⢿⡀⠿⣿⣿⣿⣿⠟⢠⡿⠿⡟⣸⣿⣷⣦⣤⣈⣉⡙⠛⠛⠛⡋⠁⢰⣿⣿
⣿⣿⣷⠀⠘⣦⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡵⠦⣤⣭⣭⡤⠴⢥⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢀⣾⠁⢀⣿⣿⣿
⣿⣿⣿⣧⠀⠸⣷⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⢀⡀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⢠⣾⠃⢀⣾⣿⣿⣿
⣿⣿⣿⣿⣧⠀⠙⣿⣄⠀⠈⠙⠛⠛⠉⠉⠉⠀⠀⠀⠀⣰⣿⣿⣄⠀⠀⠀⠀⠉⠉⠉⠙⠛⠋⠀⠀⣰⡿⠃⢀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠈⠻⣦⣄⣀⣀⣀⣀⣀⡀⠀⠀⠀⠾⠿⠿⠿⠿⠦⠀⠀⠀⣀⣀⣀⣀⣀⣀⣠⣾⠟⠀⢀⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣄⠐⣦⡙⠿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⠟⣋⡴⠁⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⡘⢿⣷⣶⣭⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣯⣭⣶⣾⡿⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⠟⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡙⢿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
               
""")
for c in x:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
        #i'm god man
        
print(f"\033[32m")
time.sleep(1)
# کلمه مورد نظر
text = "P O R Y _ G O D"

# ایجاد متن بزرگ و افکت دار
large_text = pyfiglet.figlet_format(text, font="slant")

# چاپ کردن متن بزرگ
print(large_text)

user_input = input("guid target:")

result = f"guid: {user_input} "
# نمایش نتیجه
print(result)

print(f"\033[36m")


    
    
    # تعداد شمارش
n = 100  # به عنوان مثال 5 عدد رندوم

# تولید لیست رندوم
random_numbers = [random.randint(1, 10000000) for _ in range(n)]  # اعداد رندوم بین 1 تا 100

# چاپ لیست به صورت عمودی با فاصله 2 ثانیه
for number in random_numbers:
    print(f"attached target number (android) {number}")
    print(f"hack.....")
    print(f"PORY")
    time.sleep(0.3)  # توقف به مدت 2 ثانیه
     
# نمایش متن پس از شمارش
time.sleep(4)
print(" ")
print("Target number successfully cracked!")
print("Target number: 9216753833.")
print("PORY")