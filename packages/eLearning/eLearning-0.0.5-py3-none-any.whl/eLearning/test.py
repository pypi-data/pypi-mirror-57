def run():

	import eLearning as el
	#-----------------------------------------------
	# Connector level operations
	#-----------------------------------------------

	elc = el.eLearning_connector()
	print(elc.client)
	print(elc.db)
	print(elc.db.list_collection_names())

	elc._tabula_rasa()

	## User managenment.

	elc.insert_professor( 'Paul Erdős', 'erdos@princeton.edu' )
	elc.insert_professor( 'Elias Menachem Stein', 'stein@princeton.edu' )
	elc.insert_student( 'Terence Tao', 'tao@princeton.edu' )
	elc.insert_student( 'Joseph Kruskal', 'kruskal@princeton.edu' )
	elc.insert_student( 'Bonifac Donat', 'donat@princeton.edu' )

	print( '\nProfessors:\n',elc.list_professors() )
	print( '\nStudents:\n',elc.list_students() )

	elc.delete_user_by_email( 'donat@princeton.edu' )

	print( '\nStudents (again):\n',elc.list_students() )

	p0 = elc.get_user_by_email( 'erdos@princeton.edu' )
	p1 = elc.get_user_by_email( 'stein@princeton.edu' )
	s0 = elc.get_user_by_email( 'tao@princeton.edu' )
	s1 = elc.get_user_by_email( 'kruskal@princeton.edu' )


	#-----------------------------------------------
	# Professor level operations
	#-----------------------------------------------

	## Course management.

	course_details= {	'title':'Arithmetic',
						'code':'M0',
						'description':'Course of arith...'
					}
	p0.create_course( **course_details )
	p0.update_course( 'M0', description='Course of arithmetic.' )


	course_details= {	'title':'Geometry',
						'code':'M1',
						'description':'Course of ...'
					}
	p1.create_course( **course_details )
	p0.delete_course( 'M1' )


	course_details= {	'title':'Algebra',
						'code':'M1',
						'description':'Course of algebra.',
						'required_course_code':'M0'
					}
	p0.create_course( **course_details )


	## Lesson management.

	lesson_details= {	'title':'Addition',
						'code':'M0L0',
						'content':'2+3=(1+1)+(1+1+1)=1+1+1+1+1=5',
						'approval_score':0.8,
						'parent_course_code':'M0'
					}
	p0.create_lesson( **lesson_details )


	lesson_details= {	'title':'Multiplication',
						'code':'M0L1',
						'content':'2*3=2+2+2=6=3+3=3*2',
						'approval_score':0.7,
						'parent_course_code':'M0',
						'required_lesson_code':'M0L0'
					}
	p1.create_lesson( **lesson_details )


	lesson_details= {	'title':'Exponentiation',
						'code':'M0L2',
						'content':'2^3=2*2*2=(2+2)+(2+2)=2+2+2+2=8',
						'approval_score':0.7,
						'parent_course_code':'M0',
						'required_lesson_code':'M0L1'
					}
	p0.create_lesson( **lesson_details )
	p1.update_lesson( 'M0L2', approval_score=0.6 )


	## Question management.

	question_details = {	'code':'M0L0Q0',
							'mode':'Bool',
							'content':{'Q':'4+5=6+3 ?'},
							'correct_answers':[True],
							'parent_lesson_code':'M0L0'
						}
	p0.create_question( **question_details )

	question_details = {	'code':'M0L0Q1',
							'mode':'Bool',
							'content':{'Q':'(3+2)+7=(1+2)+(3+7) ?'},
							'correct_answers':[False],
							'parent_lesson_code':'M0L0'
						}
	p1.create_question( **question_details )

	question_details = {	'code':'M0L0Q2',
							'mode':'Bool',
							'content':{'Q':'(1+1+1+1+1)+(1+1+(1+1))=((1+1+1)+1)+1+(1+1+1+1) ?'},
							'correct_answers':[False],
							'parent_lesson_code':'M0L0'
						}
	p1.create_question( **question_details )
	p0.update_question( 'M0L0Q2', correct_answers=[True] )

	#-----------------------------------------------

	question_details = {	'code':'M0L1Q0',
							'mode':'MC1A',
							'content':{'Q':'7*3= ?','A':'7*7*7', 'B':'7+7+7', 'C':'24'},
							'correct_answers':['B'],
							'parent_lesson_code':'M0L1'
						}
	p1.create_question( **question_details )

	question_details = {	'code':'M0L1Q1',
							'mode':'MC1A',
							'content':{'Q':'-3*1= ?','A':'-1-1-1', 'B':'3'},
							'correct_answers':['A'],
							'parent_lesson_code':'M0L1'
						}
	p1.create_question( **question_details )

	question_details = {	'code':'M0L1Q2',
							'mode':'MCMA+',
							'content':{'Q':'-5*3= ?','A':'5-5-5', 'B':'-3-3-3-(3+3)', 'C':'-2*3-3*3'},
							'correct_answers':['B','C'],
							'parent_lesson_code':'M0L1'
						}
	p0.create_question( **question_details )

	#-----------------------------------------------

	question_details = {	'code':'M0L2Q0',
							'mode':'MCMA+',
							'content':{'Q':'7^3= ?','A':'7*7*7', 'B':'3*3*3*3*3*3*3', 'C':'7^2*7'},
							'correct_answers':['A','C'],
							'parent_lesson_code':'M0L2'
						}
	p1.create_question( **question_details )

	question_details = {	'code':'M0L2Q1',
							'mode':'MCMA*',
							'content':{'Q':'3^0= ?','A':'3/3', 'B':'1', 'C':'0'},
							'correct_answers':['A','B'],
							'parent_lesson_code':'M0L2'
						}
	p0.create_question( **question_details )
	p1.delete_question( 'M0L2Q1' )

	question_details = {	'code':'M0L2Q1',
							'mode':'MCMA*',
							'content':{'Q':'3^1*3^2*9= ?','A':'(3)*(3*3)*(3*3)', 'B':'3^5', 'C':'3*3^4', 'D':'None'},
							'correct_answers':['A','B','C'],
							'parent_lesson_code':'M0L2'
						}
	p0.create_question( **question_details )

	question_details = {	'code':'M0L2Q2',
							'mode':'MCMA*',
							'content':{'Q':'-5^2≠ ?','A':'(-5)*(-5)', 'B':'5*5', 'C':'None'},
							'correct_answers':['A','B'],
							'parent_lesson_code':'M0L2'
						}
	p0.create_question( **question_details )


	## Course, Lesson and Question reading.

	C = p0.list_courses()
	print( '\nCourses:\n',C)

	print( '\nCourse M0\n',p0.read_course('M0') )

	print( '\nFull course M0\n',p0.read_course('M0',True) )

	print( '\nLesson M0L2\n',p1.read_lesson('M0L2') )

	print( '\nQuestion M0L2Q1\n',p1.read_question('M0L2Q1') )


	#-----------------------------------------------
	# Student level operations
	#-----------------------------------------------

	## Check courses and lessons availability for student "s0".

	print( '\nCourses for {student}\n'.format(student=s0.fullname),s0.list_courses_and_availability() )

	L = s0.list_lessons_and_availability('M0')
	print( '\nLessons for {student}\n'.format(student=s0.fullname),type(L) )
	for l in L:
		print( '\n',l )


	## Student "s0" tries to get full lesson's information. 

	print( '\nGet full lesson M0L1 for {student}\n'.format(student=s0.fullname),s0.get_full_lesson('M0L1') )
	print( '\nGet full lesson M0L0 for {student}\n'.format(student=s0.fullname),s0.get_full_lesson('M0L0') )


	## Student "s0" takes an available lesson.

	print( '\n\n{student} takes lesson M0L0:'.format(student=s0.fullname) )
	print( s0.take_lesson( 'M0L0', [[True],[False],[True]] ))


	## Check lessons availability for student "s0".

	L = s0.list_lessons_and_availability('M0')
	print( '\nLessons for {student}\n'.format(student=s0.fullname),type(L) )
	for l in L:
		print( '\n',l )


	## Check lessons availability for student "s1".

	L = s1.list_lessons_and_availability('M0')
	print( '\nLessons for {student}\n'.format(student=s1.fullname),type(L) )
	for l in L:
		print( '\n',l )


	## Student "s0" takes rest available lessons.

	print( '\n\n{student} takes lesson M0L1:'.format(student=s0.fullname) )
	print( s0.take_lesson( 'M0L1', [['B'],['A'],['C']] ))
	print( '\n\n{student} takes lesson M0L1:'.format(student=s1.fullname) )
	print( s1.take_lesson( 'M0L1', [['B'],['A'],['C']] ))
	print( '\n\n{student} takes lesson M0L2:'.format(student=s0.fullname) )
	print( s0.take_lesson( 'M0L2', [['C'],['A','B','C'],['A']] ))


	## Check courses availability for both students.

	print( '\n\n',s0.list_courses_and_availability() )
	print( '\n\n',s1.list_courses_and_availability() )


	## Get record summary for student "s0".

	print( '\n\n\n',s0.get_record_summary() )




