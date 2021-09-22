import random
import string
import os
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
s=[]
a=str(input("do you want uppercase in your password--(Y/N)--"))
b=str(input("do you want lowercase in your password--(Y/N)--"))
c=str(input("do you want digits in your password--(Y/N)--"))
d=str(input("do you want special characters in your password--(Y/N)--"))
if(a=="Y" or a=="y"):
    s.extend(list(s1))
    os.system('cls')
elif(a=="n" or a=="N"):
    os.system('cls')
    pass
else:
    print("invalid input!!")
    os.system('cls')
    exit()
if(b=="Y" or b=="y"):
    s.extend(list(s2))
    os.system('cls')
elif(b=="n" or b=="N"):
    os.system('cls')
    pass
else:
    print("invalid input!!")
    os.system('cls')
    exit()
if(c=="Y" or c=="y"):
    s.extend(list(s3))
    os.system('cls')
elif(c=="n" or c=="N"):
    os.system('cls')
    pass    
else:
    print("invalid input!!")
    os.system('cls')
    exit()
if(d=="Y" or d=="y"):
    s.extend(list(s4))
    os.system('cls')
elif(d=="n" or d=="N"):
    os.system('cls')
    pass
else:
    print("invalid input!!")
    os.system('cls')
    exit()
random.shuffle(s)
n=int(input("Enter the length of password you want--"))
print("Your generated password is---\n")
print("".join(s[0:n]))
    
