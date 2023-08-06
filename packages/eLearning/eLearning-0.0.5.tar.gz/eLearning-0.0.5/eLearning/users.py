import pymongo
import bson


class eLearning_professor():

	def __init__( self, connector, document ):
		
		self._id = document['_id']
		self.fullname = document['fullname']
		self.role = document['role']
		self.email = document['email']
		self._connector = connector
 

	def create_course( self, title, code, description=None, required_course_code=None ):

		result = list(self._connector.course_collection.find( {'code':code} ))
		if len(result)>0:
			return ('400 - Bad Request',"Course's code already exists.")
		
		document = {	'title':title,
						'code':code,
						'autor_id':self._id,
						'description':description  }

		if required_course_code!=None:
			required_course = self._connector.course_collection.find_one( {'code':required_course_code} )
			if required_course==None:
				return ('404 - Not Found',"Required-course's code not found.")
			
			document['required_course_code'] = required_course['code']
			document['required_course_id'] = required_course['_id']
		else:
			document['required_course_code'] = None
			document['required_course_id'] = None

		result = self._connector.course_collection.insert_one( document )

		if result==None:
			return ('409 - Conflict',"Insertion error.")
		elif isinstance(result.inserted_id, bson.ObjectId):
			self._connector._insert_binnacle('professor', 'course', self._id, result.inserted_id, 'C')
			return ('200 - OK',"")


	def create_lesson( self, title, code, content, parent_course_code, approval_score=1.0, required_lesson_code=None ):

		result = list(self._connector.lesson_collection.find( {'code':code} ))
		if len(result)>0:
			return ('400 - Bad Request',"Lesson's code already exists.")
		
		parent_course = self._connector.course_collection.find_one( {'code':parent_course_code} )
		if parent_course==None:
			return ('404 - Not Found',"Parent-course's code not found.")

		if approval_score>1.0 or approval_score<0.0:
			return ('400 - Bad Request',"Invalid approval-score.")

		document = {	'title':title,
						'code':code,
						'autor_id':self._id,
						'content':content,
						'approval_score':approval_score,
						'parent_course_code':parent_course['code'],
						'parent_course_id':parent_course['_id'] }

		if required_lesson_code!=None:
			required_lesson = self._connector.lesson_collection.find_one( {'code':required_lesson_code} )
			if required_lesson==None:
				return ('404 - Not Found',"Required-lesson's code not found.")

			document['required_lesson_code'] = required_lesson['code']
			document['required_lesson_id'] = required_lesson['_id']
		else:
			document['required_lesson_code'] = None
			document['required_lesson_id'] = None

		result = self._connector.lesson_collection.insert_one( document )

		if result==None:
			return ('409 - Conflict',"Insertion error.")
		elif isinstance(result.inserted_id, bson.ObjectId):
			self._connector._insert_binnacle('professor', 'lesson', self._id, result.inserted_id, 'C')
			return ('200 - OK',"")


	def create_question( self, code, mode, content, correct_answers, parent_lesson_code ):

		if not mode in ['Bool','MC1A','MCMA+','MCMA*']:
			return ('400 - Bad Request',"Invalid question mode.")

		if not isinstance(correct_answers, list):
			return ('400 - Bad Request',"Answers have to be a list of strings.")

		parent_lesson = self._connector.lesson_collection.find_one( {'code':parent_lesson_code} )
		if parent_lesson==None:
			return ('404 - Not Found',"Parent-lesson's code not found.")
		
		document = {	'code':code,
						'autor_id':self._id,
						'mode':mode,
						'content':content,
						'correct_answers':correct_answers,
						'parent_lesson_code':parent_lesson['code'],
						'parent_lesson_id':parent_lesson['_id'],
						'parent_course_code':parent_lesson['parent_course_code'],
						'parent_course_id':parent_lesson['_id'] }

		result = self._connector.question_collection.insert_one( document )

		if result==None:
			return ('409 - Conflict',"Insertion error.")
		elif isinstance(result.inserted_id, bson.ObjectId):
			self._connector._insert_binnacle('professor', 'question', self._id, result.inserted_id, 'C')
			return ('200 - OK',"")


	def list_courses( self ):

		courses = list(self._connector.course_collection.find())
		return courses


	def read_course( self, code, full=False ):

		course = self._connector._get_course( code, full )
		if course!=None:
			self._connector._insert_binnacle('professor', 'course', self._id, course['_id'], 'R')
		return course


	def read_lesson( self, code, full=False ):

		lesson = self._connector._get_lesson( code, full )
		if lesson!=None:
			self._connector._insert_binnacle('professor', 'lesson', self._id, lesson['_id'], 'R')
		return lesson


	def read_question( self, code ):

		question = self._connector._get_question( code )
		if question!=None:
			self._connector._insert_binnacle('professor', 'question', self._id, question['_id'], 'R')
		return question


	def update_course( self, code, **kwargs ):

		course = self._connector.course_collection.find_one( {'code':code} )
		count = 0
		for key,value in kwargs.items():
			if key in course:
				if key!='code' and key!='_id':
					result = self._connector.course_collection.update_one( {'code':code},{'$set':{key:value}} )
					count += result.modified_count
		if count:
			self._connector._insert_binnacle('professor', 'course', self._id, course['_id'], 'U')
			print(count,'updates.')
			return count


	def update_lesson( self, code, **kwargs ):

		lesson = self._connector.lesson_collection.find_one( {'code':code} )
		count = 0
		for key,value in kwargs.items():
			if key in lesson:
				if key!='code' and key!='_id':
					result = self._connector.lesson_collection.update_one( {'code':code},{'$set':{key:value}} )
					count += result.modified_count
		if count:
			self._connector._insert_binnacle('professor', 'lesson', self._id, lesson['_id'], 'U')
			print(count,'updates.')
			return count


	def update_question( self, code, **kwargs ):

		question = self._connector.question_collection.find_one( {'code':code} )
		count = 0
		for key,value in kwargs.items():
			if key in question:
				if key!='code' and key!='_id':
					result = self._connector.question_collection.update_one( {'code':code},{'$set':{key:value}} )
					count += result.modified_count
		if count:
			self._connector._insert_binnacle('professor', 'question', self._id, question['_id'], 'U')
			print(count,'updates.')
			return count


	def delete_course( self, code ):

		course = self._connector.course_collection.find_one( {'code':code} )
		count = 0
		result = self._connector.question_collection.delete_many( {'parent_course_code':code} )
		count += result.deleted_count
		result = self._connector.lesson_collection.delete_many( {'parent_course_code':code} )
		count += result.deleted_count
		result = self._connector.course_collection.delete_one( {'code':code} )
		count += result.deleted_count
		if count:
			self._connector._insert_binnacle('professor', 'course', self._id, course['_id'], 'D')
			print(count,'deletions.')
			return count


	def delete_lesson( self, code ):

		lesson = self._connector.lesson_collection.find_one( {'code':code} )
		count = 0
		result = self._connector.question_collection.delete_many( {'parent_course_code':code} )
		count += result.deleted_count
		result = self._connector.lesson_collection.delete_one( {'code':code} )
		count += result.deleted_count
		if count:
			self._connector._insert_binnacle('professor', 'lesson', self._id, lesson['_id'], 'D')
			print(count,'deletions.')
			return count


	def delete_question( self, code ):

		question = self._connector.question_collection.find_one( {'code':code} )
		result = self._connector.question_collection.delete_one( {'code':code} )
		count = result.deleted_count
		if count:
			self._connector._insert_binnacle('professor', 'question', self._id, question['_id'], 'D')
			print(count,'deletions.')
			return count


	def _get_binnacle( self ):

		_binnacle = self._connector.binnacle_collection.find({'subject_id':self._id})
		return _binnacle



class eLearning_student():

	def __init__( self, connector, document ):
		
		self._id = document['_id']
		self.fullname = document['fullname']
		self.role = document['role']
		self.email = document['email']
		self.score = document['score']
		self._connector = connector
		self._update_approved_course_ids()
		self._update_approved_lesson_ids()
 

	def get_record_summary( self ):

		documents = list(self._connector.record_collection.find( {	'subject_id':self._id,
																	'status':'approved'}   ))
		resume = []
		for document in documents:
			resume.append( 	{	'type':document['object_type'],
								'code':document['object_code'],
								'status':document['status'],
								'score':document['score'],
								'datetime':document['datetime']
							} )
		return resume


	def list_courses_and_availability( self ):

		courses = list(self._connector.course_collection.find())

		for course in courses:
			if course['_id'] in self._approved_course_ids:
				course['available'] = True
			elif course['required_course_id'] in self._approved_course_ids:
				course['available'] = True
			elif course['required_course_id']==None:
				course['available'] = True
			else:
				course['available'] = False

		return courses


	def list_lessons_and_availability( self, parent_course_code ):

		lessons = list(self._connector.lesson_collection.find( {'parent_course_code':parent_course_code} ))

		for lesson in lessons:
			if lesson['_id'] in self._approved_lesson_ids:
				lesson['available'] = True
			elif lesson['required_lesson_id'] in self._approved_lesson_ids:
				lesson['available'] = True
			elif lesson['required_lesson_id']==None:
				lesson['available'] = True
			else:
				lesson['available'] = False

		return lessons


	def get_full_lesson( self, code ):

		lesson = self._connector._get_lesson( code, True )

		if lesson['_id'] in self._approved_lesson_ids:
			pass
		elif lesson['required_lesson_id'] in self._approved_lesson_ids:
			pass
		elif lesson['required_lesson_id']==None:
			pass
		else:
			return None

		self._connector._insert_binnacle('student', 'lesson', self._id, lesson['_id'], 'R')
		return lesson


	def take_lesson( self, code, answers_list ):

		lesson = self._connector._get_lesson( code, True )

		try:
			if lesson['_id'] in self._approved_lesson_ids:
				pass
			elif lesson['required_lesson_id'] in self._approved_lesson_ids:
				pass
			elif lesson['required_lesson_id']==None:
				pass
			else:
				return None
			self._connector._insert_binnacle('student', 'lesson', self._id, lesson['_id'], 'T')
			return self._check_answers_for_lesson( lesson, answers_list )

		except AssertionError:
			raise ValueError("Answers' labels are not congruence or some question hasn't be answered.")


	def _check_answers_for_lesson( self, lesson, answers_list ):

		assert( len(lesson['questions'])==len(answers_list) )

		numof_questions = len(lesson['questions'])
		iscorrect_count = 0

		for question, answers in zip( lesson['questions'], answers_list ):
			correct_answers = question['correct_answers']

			if question['mode'] == 'Bool':
				assert( isinstance(correct_answers[0],bool) )
				assert( isinstance(answers[0],bool) )
				if len(correct_answers)!=1 or len(answers)!=1:
					continue

				if correct_answers[0]==answers[0]:
					iscorrect_count +=1

			elif question['mode'] == 'MC1A':
				assert( isinstance(correct_answers[0],str) )
				assert( isinstance(answers[0],str) )
				if len(correct_answers)!=1 or len(answers)!=1:
					continue

				if correct_answers[0]==answers[0]:
					iscorrect_count +=1

			elif question['mode'] == 'MCMA+':
				if len(correct_answers)<len(answers):
					continue

				correct_answers = set(correct_answers)
				answers = set(answers)

				if (correct_answers|answers)==correct_answers:
					iscorrect_count +=1

			elif question['mode'] == 'MCMA*':
				if len(correct_answers)!=len(answers):
					continue

				correct_answers = set(correct_answers)
				answers = set(answers)

				if correct_answers==answers:
					iscorrect_count +=1

			else:
				raise TypeError('Incorrect question mode.')
		
		score = iscorrect_count/numof_questions

		if score>=lesson['approval_score']:
			
			self._connector._insert_record( 'lesson', self._id, lesson['_id'], lesson['code'], 'approved', score )
			self._update_approved_lesson_ids()	
			
			if self._check_parent_course_is_approved( lesson['parent_course_id'] ):
				return {'lesson':{'score':score,'status':'approved'},'course':{'status':'approved'}}
			
			return {'lesson':{'score':score,'status':'approved'}}
		
		else:
			return {'lesson':{'score':score,'status':'failed'}}


	def _check_parent_course_is_approved( self, parent_course_id ):

		lessons = list(self._connector.lesson_collection.find(	{'parent_course_id':parent_course_id} ))
		for lesson in lessons:
			approved_lesson = self._connector.record_collection.find_one(	{	'object_type':'lesson',
																				'subject_id':self._id,
																				'object_id':lesson['_id'],
																				'status':'approved'    
																			} )
			if approved_lesson==None:
				return False

		self._connector._insert_record( 'course', self._id, parent_course_id, lesson['parent_course_code'], 'approved' )
		self._update_approved_course_ids()
		return True


	def _update_approved_course_ids( self ):

		extract_id = lambda D: D['object_id']
		documents = list(self._connector.record_collection.find( {	'subject_id':self._id,
																	'object_type':'course',
																	'status':'approved'}, {'object_id':1} ))
		self._approved_course_ids = list(map(extract_id, documents))


	def _update_approved_lesson_ids( self ):

		extract_id = lambda D: D['object_id']
		documents = list(self._connector.record_collection.find( {	'subject_id':self._id,
																	'object_type':'lesson',
																	'status':'approved'}, {'object_id':1} ))
		self._approved_lesson_ids = list(map(extract_id, documents))


	def _get_binnacle( self ):

		_binnacle = self._connector.binnacle_collection.find({'subject_id':self._id})
		return _binnacle


