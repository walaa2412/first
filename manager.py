def signup():
	print("Please enter the username by which you \
	wanna access your account")
	username = input("please enter here: ")
	password = input("Enter a password: ")
# pssd means password, ussnm is username
def user_information(ussnm, pssd):
	name = input("enter your name please: ")
	address = input("your address")
	age = input("Your age please")
	ussnm_ = ussnm+" task.txt"
	
	f = open(ussnm_, 'a')
	f.write(pssd)
	f.write("\nName: ")
	f.write(name)
	f.write('\n')
	f.write("Address :")

	f.write(address)
	f.write('\n')
	f.write("Age :")
	f.write(age)
	f.write('\n')
	f.close()


def signup():
	print("Please enter the username by which you\
	wanna access your account")
	username = input("please enter here: ")
	password = input("Enter a password: ")
	user_information(username, password)
def login():
	print("Please enter your username ")
	user_nm = input("Enter here: ")
	
	# Password as entered while logging in
	pssd_wr = (input("enterr the password"))+'\n'
	try:
		usernm = user_nm+" task.txt"
		f_ = open(usernm, 'r')
		
		# variable 'k' contains the password as saved
		# in the file
		k = f_.readlines(0)[0]
		f_.close()
		
		# Checking if the Password entered is same as
		# the password saved while signing in
		if pssd_wr == k: 
			print(
				"1--to view your data \n2--To add task \n3--Update\
				task status \n4--View task status")
			a = input()
		else:
			print("SIR YOUR PASSWORD OR USERNAME IS WRONG , Plz enter Again")
			login()
	except Exception as e:
		print(e)
		login()
def signup():
	print("Please enter the username by which you wanna access your account")
	username = input("please enter here: ")
	password = input("Enter a password: ")
	user_information(username, password)
	print("Sir please proceed towards log in")
	login()
def login():
	print("Please enter your username ")
	user_nm = input("Enter here: ")
	
	# Password as entered while logging in
	pssd_wr = (input("enterr the password"))+'\n'
	try:
		usernm = user_nm+" task.txt"
		f_ = open(usernm, 'r')
		
		# variable 'k' contains the password as
		# saved in the file
		k = f_.readlines(0)[0]
		f_.close()
		
		# Checking if the Password entered is same
		# as the password saved while signing in
		if pssd_wr == k: 
			print(
				"1--to view your data \n2--To add task \n3--Update\
				task \n4--VIEW TASK STATUS")
			a = input()
			
			if a == '1':
				view_data(usernm)
			elif a == '2':
				# add task
				task_information(usernm)
			elif a == '3':
				task_update(user_nm)
			elif a == '4':
				task_update_viewer(user_nm)
			else:
				print("Wrong input ! ")
		else:
			print("SIR YOUR PASSWORD OR USERNAME IS WRONG")
			login()

	except Exception as e:
		print(e)
		login()


def view_data(username):
	pass

def task_information(username):
	pass

def task_update(username):
	pass

def task_update_viewer(username):
	pass
def view_data(username):
	ff = open(username, 'r')
	print(ff.read())
	ff.close()
def task_information(username):
	print("Sir enter n.o of task you want to ADD")
	j = int(input())
	f1 = open(username, 'a')
	
	for i in range(1, j+1):
		task = input("enter the task")
		target = input("enter the target")
		pp = "TASK "+str(i)+' :'
		qq = "TARGET "+str(i)+" :"
		
		f1.write(pp)
		f1.write(task)
		f1.write('\n')
		f1.write(qq)
		f1.write(target)
		f1.write('\n')
		
		print("Do u want to stop press space bar otherwise enter")
		s = input()
		if s == ' ':
			break
	f1.close()
