from random import *

user_pass = input("Enter Your Password: ")
password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

guess__= ""

while (guess__ != user_pass):
    guess = ""
    for latter in range (len(user_pass)):
        guess_latter = password [randint(0,25)]
        guess = str(guess_latter) + str(guess)
        print(guess)
print("Your Correct password is ", guess)

