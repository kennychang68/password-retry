pwd = 'rt123456'
x = 3
while x>0:
	password = input('please type your password')
	if password == pwd:
		print('password is correct')
		break
	else:
		print('password is wrong')
	x = x - 1
	print(x ,'chance left')
