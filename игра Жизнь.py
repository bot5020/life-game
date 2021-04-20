import os
import random
import time

def print_mass(mass):
    os.system('cls') 
    for i in mass:
        print(i)
     
n = 10
m = 10
while True:
    mass = []  
    for i in range(n):
        mass.append([random.randrange(0, 2) for i in range(m)])
    print_mass(mass)
    time.sleep(2)

#[random.randrange(0, 3,2) for i in range(m)]
#print_mass(mass)    
    


