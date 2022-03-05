from random import *

password = input ("\n Enter your password : ")
letters = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guess = ""


while guess != password :
    guess = ""
    for letter in range(len(password)):
        guess_letter =  letters[randint(0,25)]
        guess = str(guess_letter) + str(guess)
        print(guess)

print("\n your password is ", guess)
print("\n thanks for using")

