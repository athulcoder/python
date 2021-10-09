command =""
print(''' Welcome.....
         
        Enter 'go' to start''')


def home():
         print('''
         
         COMMANDS	    
car --- to start the car game  
quit  --- to quit 
home --- to return home
Enter' Any Above Command'  ''')


def help1():
         print('''
         
         COMMANDS	    
car   --- to start the car game  
quit  --- to quit 
go    --- to return home

Enter' Any Above Command'

    ''')

        

def car():
		start = False  
		print("""     __Car Game__ """.upper())
		print(''' 
start -- to start the car
stop -- to  stop the car 
quit  -- to quit the Game
''')		
		
		while True:
		           
		           car_command = input(">>>")
		           if car_command=='start':
		           	if start:
		           		print(' What is this!! Car is already  started......')
		           	else:
		           	   	start= True
		           	   	print('car Started...... ')
		           elif car_command =='stop':
		          		if not start:
		          			print("Car is already stopped......")
		           
		          		else:
		          			start=False
		          			print("Car Stopped")
		           elif car_command=='quit':
		           	print("Enter'go' to return home")
		           	return home
		           else:
		           	print("Sorry I Couldn't Understand You ....Enter Any Above Command")
		          		

def quit():
	    while True:
	    	break		          	
				
				
		
while True:
	command = input('>')
	if command =='y':
		
		print('Welcome to my home ...! . To Start a Coversation Enter "go" ')
	elif command =='go':
		help1()
	elif command =='car':
	    car()
	elif command =='quit':
	 	quit()
	elif command not in('go','car','quit'):
	 	print('Wrong Command, Enter "go" ')

