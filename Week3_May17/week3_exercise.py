import sys

class Student():
	def __init__(fname, lname, grade =None):
		self.name = fname +" "+lname
		self.grade = grade 

def add_student(student):
	global student_grade_dict
	student_grade_dict[student.name] = student.grade 
	return(student_grade_dict)

'''
def find_student(student):
	global student_grade_dict
	try: 
		stored_grade = student_grade_dict[student.name]
		return(stored_grade)
	except: 
		print('There is no grade for that student')
		return('')
'''
def delete_student(student):
	global student_grade_dict
	del student_grade_dict[student.name]
	return(student_grade_dict)

# these parameters will come as input from the site 
fname = 'ashlynn'
lname = 'ste'
grade = 100
action = 'add'
student_instance = Student(fname, lname, grade)


if action == 'add': 
	add_student(student_instance)
if action == 'update': 
	add_student(student_instance)
if action == 'remove': 
	delete_student(student_instance)

'''
def triage(input1):
	global student_grade_dict
	if input1 == 'add': 
		name = input('Please enter the students name:')
		grade = input('Please enter their corresponding grade:')
		student_grade_dict = add_student(name, grade)
		print('Student added')

	elif input1 == 'search':
		name = input('Please enter name of student you would like to search:')
		grade = find_student(name)
		print('The students grade is: ', grade)

	elif input1 == 'update':
		name = input('Please enter name of student whose grade you would like to update:')
		grade = input('Please enter their updated grade:')
		student_grade_dict = add_student(name, grade) # overwiting current entry uses same syntax so might as well reuse
		print('Student updated')

	elif input1 == 'delete': 
		name = input('Please enter name of student you would like to delete:')
		student_grade_dict = delete_student(name)
		print('Student deleted')
	else: 
		print('Sorry your response was not recognized')

	input2 = input('Would you like to perform another opperation?[y/n]:')
	if input2 == 'y':
		input_rec = input('Would you like to add, search, update or delete? :')
		triage(input_rec) # wohoo recusion
	else:
		sys.exit()

student_grade_dict = {}
input1 = input('Would you like to add, search, update or delete? :')
triage(input1)
'''
