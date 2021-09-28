display = {
          
          "Name":"Athul Sabu",
          "Age": 14 ,
          "Father":"Sabu",
          "Mother":"Usha Antony"
}

while True:
	output= input("What U Want : ")
	if output in display:
		print(display[output])
	elif output=="n":
		break