pwd = 'rt123456'
x = 3
while x>0:
	x = x - 1
	password = input('please type your password : ')
	if password == pwd:
		print('password is correct')
		break
	else:
		print('password is wrong')
		if x > 0:
			print(x ,'chance left')
		else:
			print('no more chance ! account is locked')
