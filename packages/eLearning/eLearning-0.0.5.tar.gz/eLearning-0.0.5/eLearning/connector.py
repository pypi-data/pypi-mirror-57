import pymongo
import bson
import datetime
from eLearning.users import eLearning_professor, eLearning_student


class eLearning_connector():

	def __init__(self):

		self.client = pymongo.MongoClient("mongodb+srv://tester:1234@cluster0-0g7ar.mongodb.net/e-learning?retryWrites=true&w=majority")
		self.db = self.client.get_default_database()
		self.course_collection = self.db.courses
		self.lesson_collection = self.db.lessons
		self.question_collection = self.db.questions
		self.binnacle_collection = self.db.binnacles
		self.record_collection = self.db.records
		self.user_collection = self.db.users


	def insert_professor(self, fullname, email):

		document = {'fullname':fullname, 'email':email, 'role':'professor'}
		result = self.user_collection.insert_one( document )

		if result==None:
			return ('409 - Conflict',"Insertion error.")
		elif isinstance(result.inserted_id, bson.ObjectId):
			return ('200 - OK',"")


	def insert_student(self, fullname, email):

		document = {'fullname':fullname, 'email':email, 'role':'student', 'score':None}
		result = self.user_collection.insert_one( document )

		if result==None:
			return ('409 - Conflict',"Insertion error.")
		elif isinstance(result.inserted_id, bson.ObjectId):
			return ('200 - OK',"")


	def delete_user_by_email( self, email ):

		result = self.user_collection.delete_one({'email':email})
		
		if result.deleted_count:
			return ('200 - OK',"")
		else:
			return ('409 - Conflict',"Deletion error.")


	def get_user_by_email( self, email ):

		document = self.user_collection.find_one({'email':email})
		
		if document['role']=='professor':
			return eLearning_professor( self, document )
		elif document['role']=='student':
			return eLearning_student( self, document )
		else:
			return None


	def list_professors( self ):

		professors = list(self.user_collection.find( {'role':'professor'} ))
		return professors
	

	def list_students( self ):

		students = list(self.user_collection.find( {'role':'student'} ))
		return students


	def list_courses( self ):

		courses = list(self.course_collection.find())
		return courses


	def list_lessons( self, parent_course_code ):

		lessons = list(self.lesson_collection.find( {'parent_course_code':parent_course_code} ))
		return lessons


	def list_questions( self, parent_lesson_code ):

		questions = list(self.question_collection.find( {'parent_lesson_code':parent_lesson_code} ))
		return questions


	def _tabula_rasa( self ):

		result = self.user_collection.delete_many({})
		print(result.deleted_count,'users deleted.')
		result = self.record_collection.delete_many({})
		print(result.deleted_count,'records deleted.')
		result = self.course_collection.delete_many({})
		print(result.deleted_count,'courses deleted.')
		result = self.lesson_collection.delete_many({})
		print(result.deleted_count,'lessons deleted.')
		result = self.question_collection.delete_many({})
		print(result.deleted_count,'questions deleted.')
		result = self.binnacle_collection.delete_many({})
		print(result.deleted_count,'binnacles deleted.')


	def _insert_record( self, object_type, subject_id, object_id, object_code, status, score=None ):

		#now = strftime("%a, %d %b %Y %H:%M:%S (GMT-6)", localtime())
		now = datetime.datetime.now()

		document = {	'object_type':object_type,
						'subject_id':subject_id,
						'object_id':object_id,
						'object_code':object_code,
						'datetime':now,
						'status':status,
						'score':score			}

		result = self.record_collection.insert_one( document )

		if result==None:
			return ('409 - Conflict',"Insertion error.")
		elif isinstance(result.inserted_id, bson.ObjectId):
			return ('200 - OK',"")
	

	def _insert_binnacle( self, subject_type, object_type, subject_id, object_id, action ):

		#now = strftime("%a, %d %b %Y %H:%M:%S (GMT-6)", localtime())
		now = datetime.datetime.now()

		document = {	'subject_type':subject_type,
						'object_type':object_type,
						'subject_id':subject_id,
						'object_id':object_id,
						'datetime':now,
						'action':action			}

		result = self.binnacle_collection.insert_one( document )

		if result==None:
			return ('409 - Conflict',"Insertion error.")
		elif isinstance(result.inserted_id, bson.ObjectId):
			return ('200 - OK',"")


	def _get_course( self, code, full ):

		course = self.course_collection.find_one( {'code':code} )

		if course!=None:
			if full:
				lessons = list( self.lesson_collection.find( {'parent_course_code':course['code']}))
				for lesson in lessons:
					questions = list( self.question_collection.find( {'parent_lesson_code':lesson['code']} ))
					lesson['questions'] = questions
			else:
				lessons = list( self.lesson_collection.find( {'parent_course_code':course['code']},{'code':1} ))

			course['lessons'] = lessons
		
		return course


	def _get_lesson( self, code, full ):

		lesson = self.lesson_collection.find_one( {'code':code} )

		if lesson!=None:
			if full:
				questions = list( self.question_collection.find( {'parent_lesson_code':lesson['code']} ))
			else:
				questions = list( self.question_collection.find( {'parent_lesson_code':lesson['code']},{'code':1} ))

			lesson['questions'] = questions
		
		return lesson


	def _get_question( self, code ):

		question = self.question_collection.find_one( {'code':code} )
		return question
