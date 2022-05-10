import sys

def add_student(name, grade):
	global student_grade_dict
	student_grade_dict[name] = grade 
	return(student_grade_dict)

def find_student(name):
	global student_grade_dict
	try: 
		grade = student_grade_dict[name]
		return(grade)
	except: 
		print('There is no grade for that student')
		return('')

def delete_student(name):
	global student_grade_dict
	del student_grade_dict[name]
	return(student_grade_dict)


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
