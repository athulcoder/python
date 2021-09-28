display = {
          
          "Name":"person-name",
          "Age": age of the person,
          "Father":"Name of Father ",
          "Mother":"Name of Mother "
}

while True:
	output= input("What U Want : ")
	if output in display:
		print(display[output])
	elif output=="exit":
		break
