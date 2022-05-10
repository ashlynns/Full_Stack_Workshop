a = [1,2,3]
'''
a.append(10)
print(a)

# extend combines lists - does not add a single value 
#a.extend(10)
#print(a)

num = 3
if num >= 0: 
	if num == 0:
		print('Zero')
	print('Positive number')
else: 
	print('Negative number')

# for each loop 
sum_val = 0
for num in a: 
	sum_val = sum_val + num
# for item loop 
for i in range(2):
	print(i)
# for else loops 
for num in a:
	print(num)
else:
	print('No more items')

# while loops 
i =1 
while i<100:
	print(i**2)
	i+=i**2


def greet(name):
	print("Hello "+name+". Good Afternoon")

greet('Ashlynn')
'''

def send_email(to,subject,content):
	check = True
	return(check)
if (send_email('test@test.com', 'hi,test', 'sample')):
	print('email sent')
else:
	print('email failed')