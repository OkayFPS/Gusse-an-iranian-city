
from random import *

names = ['alborz','ardebil','bushehr','azarbaijan','esfahan','fars','gilan',
        'golestan','hamadan','hormozgan','ilam','kerman','kermanshah',
        'khuzestan','kordestan','lorestan','markazi','mazandaran','khorasan',
        'qazvin','qom','semnan','sistan','tehran','yazd','zanjan']
    
n = randint(0,len(names)-1)
name = names[n]
print(name)

charNumber = len(name)
userList = ["-"] * charNumber    
print(userList, end = '')

while "-" in userList :
    guess = input(" Guess a character: ")

    for i in range(charNumber) :
        if guess == name[i] :
            userList[i] = guess
        
    print(userList, end = '')
print("")
print(":D - You Won - Congratulations")
