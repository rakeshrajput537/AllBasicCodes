dict = {}
while True:
	print("--------Welcome To Birthday App------")
	print("1.Show Birthday")
	print("2.Add to Birthday List")
	print("3.Exit")

	choice = int(input("Enter your choice "))
	if choice==1:
		if len(dict.keys())==0:
			print("Nothing To Show")
		else:
			name = input("Enter name to look for Birthday ")
			Birthday=dict.get(name,"No data found")
			print(Birthday)
	elif choice==2:
		name=input("Enter the name ")
		date=input("enter the Birthday date ")
		dict[name]=date
		print("Birthday added")
	elif choice==3:
		break
	else:
		print("Invalid Choice")
