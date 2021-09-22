a=(('a','@'),('i','!'),("and","&"),("s","$"),('o','0'),('I','1'))
def passw(password):
    for x,y in a:
        password=password.replace(x, y)
    return password
password=str(input("enter your password---"))
print("your secure password should be--",passw(password))
