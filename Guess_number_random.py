# import randow module 
import random

#defined a funtion call main
def main():
	# defined a variable call number to store the randow number between 1 to 10
	number = int(11*(random.random()))
  # starts a while loop which is expressed as true	
	while True:
	# defined an input varible call Guess to store the integer  
		Guess = int(input("Guess : "))
# if the Guessed number is equal to the number stored in the varible call number ,it will print "you win.." and then it will ask the user  if they would like to continue the Game..
# To enter the input (y or n) of the user a varible call again is defined 

		if Guess == number:
			print("You Win ....")
			again = input("\n   Do You like to continue[y] or [n] : ")
# if the input is "y" then it will continue the Game and if the input is "n" then it will break the loop and end the Game 
			if again =="y":
				main()
			elif again == "n":
				break
			else :
				print('sorry I didn\'t get you ..')
		elif  Guess > number :
			print("The Number is less  than this Number  ")     
		elif Guess < number:
			print("The Number is more then this number  ")
			
			
			
main()
