import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, delay=0.15):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

lyrics = [
    ("Koi sone sa tole re,", 0.14, 0.4),           
    ("koi matti sa bole re", 0.14, 0.8),           
    ("Koi bole ke chaandi ka hai chhura", 0.13, 1.2),  
    ("Hota aise yeh mauke pe", 0.14, 1.4),
    ("Roka jaaye na roke se", 0.13, 0.6),
    ("Accha hota hai hota hai yeh bura", 0.14, 1.3),
    ("Kaisa yeh isq hai, ajab sa risk hai", 0.12, 1.6),   
    ("Kaisa yeh isq hai, ajab sa risk hai,", 0.11, 0.8),  
    ("ajab sa risk hai", 0.10, 3.0),                       
]

clear()
print("\n" * 15)
time.sleep(1.8)

for line, word_delay, pause in lyrics:
    clear()
    print("\n" * 12)
    print(" " * 18, end="")
    type_writer(line, delay=word_delay)        
    print("\n" * 2)
    print(" " * 28 + "." * 28)
    time.sleep(pause)                          
clear()
print("\n" * 15)
print(" " * 22, end="")
type_writer("Tu hi mera junoon hai", delay=0.20)   
time.sleep(6)

clear()
print("\n" * 12)
print(" " * 25, end="")
type_writer("Made with @Raunak-Codes..Follow For More!!", delay=0.10)
time.sleep(3)