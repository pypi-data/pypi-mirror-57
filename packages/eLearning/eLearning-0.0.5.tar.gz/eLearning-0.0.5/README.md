# eLearning API Documentation

eLearning is an API dedicated to managing the backend infrastructure of an e-learning system. eLearning is totally developed with Python 3.6+ and the data storing is a MongoDB implementation through the third-party API pymongo 3.9.0. 

## Installation

Assuming, Python 3 (>=3.6) is already installed and a [MongoDB](https://www.mongodb.com/) Cluster connection is working, eLearning API needs the next requirements:

1.	[pymongo 3.9.0](https://api.mongodb.com/python/current/). Or, it can be easily installed with:

	```
	$ python -m pip install pymongo
	```

2.	[dnspython](https://pypi.org/project/dnspython/). Or, it can be easily installed with:

	```
	$ python -m pip install pymongo[srv]
	```

3.	[pip](https://pip.pypa.io/en/stable/installing/). Or, it can be easily installed with:

	```
	$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	$ python get-pip.py
	```

4. Install with:
   
   ```
   $ pip install eLearning
   ```

5. Import and hello-world:

	```
	import eLearning as el
	elc = el.eLearning_connector()
	print(elc.client)
	print(elc.db)
	print(elc.db.list_collection_names())
	elc._tabula_rasa()
	elc.insert_professor( 'Paul Erdős', 'erdos@princeton.edu' )
	elc.insert_student( 'Terence Tao', 'tao@princeton.edu' )
	```

___

## Testing

To test the API, please try the next lines at your Python command-line interface:

	import eLearning as el
	el.eLearning_test.run()
___


## eLearning API documentation

### Connector level operations


_class **eLearning_connector** ( )_

   An eLearning_connector is the object used to communicate with MongoDB cluster and databases. eLearning_connector object has the next attributes:

   * eLearning_connector.**client** : informative dictionary about the connector.
   * eLearning_connector.**db** : informative dictionary about the database.
   * eLearning_connector.**course_collection** : MongoDB collection object with the courses information.
   * eLearning_connector.**lesson_collection** : MongoDB collection object with the lessons information.
   * eLearning_connector.**question_collection** : MongoDB collection object with the questions information.
   * eLearning_connector.**binnacle_collection** : MongoDB collection object with the binnacles information.
   * eLearning_connector.**record_collection** : MongoDB collection object with the records information.
   * eLearning_connector.**user_collection** : MongoDB collection object with the users information.
___

_eLearning_connector.**insert_professor** ( fullname, email )_

> Return the tuple `('200 - OK',"")` if the professor-user with given _fullname_ and _email_ was inserted successfully in the database. Otherwise, return `('409 - Conflict',"Insertion error.")`.


_eLearning_connector.**insert_student** ( fullname, email )_

> Return the tuple `('200 - OK',"")` if the student-user with given _fullname_ and _email_ was inserted successfully in the database. Otherwise, return `('409 - Conflict',"Insertion error.")`.


_eLearning_connector.**delete_user_by_email** ( email )_

> Return the tuple `('200 - OK',"")` if the user with given _email_ was deleted successfully from the database. Otherwise, return `('409 - Conflict',"Deletion error.")`.


_eLearning_connector.**get_user_by_email** ( email )_

> Return a _class **eLearning_professor**_ instance if the given _email_ results of a professor-user. Return a _class **eLearning_student**_ instance if the given _email_ results of a student-user. Otherwise, return `None`.


_eLearning_connector.**list_professors** ()_

> Return a Python _list_ object with all existing professor-user documents, each document is arranged into a Python _dict_ object. If there are not professor-users in database, an empty list is returned.


_eLearning_connector.**list_students** ()_

> Return a Python _list_ object with all existing student-user documents, each document is arranged into a Python _dict_ object. If there are not student-users in database, an empty list is returned.


_eLearning_connector.**list_courses** ()_

> Return a Python _list_ object with all existing course documents, each document is arranged into a Python _dict_ object. If there are not courses in database, an empty list is returned.


_eLearning_connector.**list_lessons** ( parent_course_code )_

> Return a Python _list_ object with all associated lesson documents to a given _parent_course_code_, each document is arranged into a Python _dict_ object. If there are not such lessons in database, an empty list is returned.


_eLearning_connector.**list_questions** ( parent_lesson_code )_

> Return a Python _list_ object with all associated question documents to a given _parent_lesson_code_, each document is arranged into a Python _dict_ object. If there are not such questions in database, an empty list is returned.
___


### User level operations


_class **eLearning_professor** ( )_

   An eLearning_professor instance corresponds to the valid professor-users' attributes and methods:

   * eLearning_professor.**fullname** :`<str>` Fullname of the user.
   * eLearning_professor.**email** : `<str>` e-mail address of the user.
   * eLearning_professor.**role** : `<str>` it always set as "professor".
___

_eLearning_professor.**create_course** ( title, code, description=`None`, required_course_code=`None` )_

> Parameters :
> * _title_: `<str>` Customized title for the course.
> * _code_: `<str>` Customized code for the course.
> * _description_: `<str>` Description of the course.
> * _required_course_code_: `<str>` Code of required approved-course. 

> Return the tuple `('200 - OK',"")` if the course with given parameters was created successfully in the database.  Otherwise, return `('400 - Bad Request',"Course's code already exists.")` , `('404 - Not Found',"Required-course's code not found.")` or `('409 - Conflict',"Insertion error.")`.


_eLearning_professor.**create_lesson** ( title, code, content, parent_course_code, approval_score=`1.0`, required_lesson_code=`None` )_

> Parameters :
> * _title_: `<str>` Customized title for the lesson.
> * _code_: `<str>` Customized code for the lesson.
> * _content_: `<str>` Description of the lesson.
> * _correct_answers_: `<list>` List of the correct answer labels (`<str>`).
> * _parent_course_code_: `<str>` Code of the parent-course.
> * _approval_score_: `<float>` Floating number between `0.0` (minimal score) and `1.0` (maximal score).
> * _required_lesson_code_: `<str>` Code of required approved-lesson. 

> Return the tuple `('200 - OK',"")` if the lesson with given parameters was created successfully in the database.  Otherwise, return `('400 - Bad Request',"Lesson's code already exists.")` , `('404 - Not Found',"Required-lesson's code not found.")` , `('404 - Not Found',"Parent-course's code not found.")` or `('409 - Conflict',"Insertion error.")`.


_eLearning_professor.**create_question** ( code, mode, content, correct_answers, parent_lesson_code )_

> Parameters :
> * _code_: `<str>` Customized code for the question.
> * _mode_: `<str>` "Bool","MC1A","MCMA\+","MCMA\*" only.
> * _content_: `<str>` Description of the question.
> * _correct_answers_: `<list>` List of option labels.
> * _parent_lesson_code_: `<str>` Code of the parent-course.

> Return the tuple `('200 - OK',"")` if the question with given parameters was created successfully in the database.  Otherwise, return `('400 - Bad Request',"Invalid question mode.")` , `('400 - Bad Request',"Answers have to be a list of strings.")`, `('404 - Not Found',"Parent-lesson's code not found.")` or `('409 - Conflict',"Insertion error.")`.


_eLearning_professor.**list_courses** ( )_

> Return the Python object _list_ with all current courses. 


_eLearning_professor.**read_course** ( code, full=`False` )_

> Parameters :
> * _code_: `<str>` Code of the course.
> * _full_: `<bool>` `False` or `True`.

> Return the Python object _dict_ with the given course attributes at creation time. Moreover, if _full_ is set to `True`, the information of all subscribed lessons and questions will be included.


_eLearning_professor.**read_lesson** ( code, full=`False` )_

> Parameters :
> * _code_: `<str>` Code of the lesson.
> * _full_: `<bool>` `False` or `True`.

> Return the Python object _dict_ with the given lesson attributes at creation time. Moreover, if _full_ is set to `True`, the information of all subscribed questions will be included.


_eLearning_professor.**read_question** ( code )_

> Parameters :
> * _code_: `<str>` Code of the question.

> Return the Python object _dict_ with the given question attributes at creation time.


_eLearning_professor.**update_course** ( code, \*\*kwards )_

> Parameters :
> * _code_: `<str>` Code of the course.
> * _\*\*kwards_: `<dict>` Dictionary with the attributes to update for the given course.

> Return an integer with the count of modified attributes.


_eLearning_professor.**update_lesson** ( code, \*\*kwards )_

> Parameters :
> * _code_: `<str>` Code of the lesson.
> * _\*\*kwards_: `<dict>` Dictionary with the attributes to update for the given lesson.

> Return an integer with the count of modified attributes.


_eLearning_professor.**update_question** ( code, \*\*kwards )_

> Parameters :
> * _code_: `<str>` Code of the question.
> * _\*\*kwards_: `<dict>` Dictionary with the attributes to update for the given question.

> Return an integer with the count of modified attributes.


_eLearning_professor.**delete_course** ( code, \*\*kwards )_

> Parameters :
> * _code_: `<str>` Code of the course.

> Return an integer with the count of deleted objects.


_eLearning_professor.**delete_lesson** ( code, \*\*kwards )_

> Parameters :
> * _code_: `<str>` Code of the lesson.

> Return an integer with the count of deleted objects.


_eLearning_professor.**delete_question** ( code, \*\*kwards )_

> Parameters :
> * _code_: `<str>` Code of the question.

> Return an integer with the count of deleted objects.
___


_class **eLearning_student** ( )_

   An eLearning_student instance corresponds to the valid student-users' attributes and methods:

   * eLearning_student.**fullname** :`<str>` Fullname of the user.
   * eLearning_student.**email** : `<str>` e-mail address of the user.
   * eLearning_student.**role** : `<str>` it always set as "student".
   * eLearning_student.**score** : `<float>` Main score.
___

_eLearning_student.**get_record_summary** ( )_

> Return a Python object _list_ with informative _dict_ about the type, code, status, score and datetime of all courses and lessons taken by the student.


_eLearning_student.**list_courses_and_availability** ( )_

> Return a Python object _list_ with all current courses. Every course is represented by an informative _dict_, where the key `'available'` indicate with `True`, whether the course is available for the student or with `False` otherwise.


 _eLearning_student.**list_lessons_and_availability** ( parent_course_code )_

> Parameters :
> * parent_course_code: `<str>` Code of the parent-course.

> Return a Python object _list_ with all current lessons. Every lesson is represented by an informative _dict_, where the key `'available'` indicate with `True`, whether the lesson is available for the student or with `False` otherwise.


_eLearning_student.**get_full_lesson** ( code )_

> Parameters :
> * code: `<str>` Code of the claimed lesson.

> Return a Python object _dict_ with the claimed lesson information and its subscrited questions.


_eLearning_student.**take_lesson** ( code, answers_list )_

> Parameters :
> * code: `<str>` Code of the taken lesson.
> * answer_list: `<list>` List with lists of the correct answers labels; _e.g._ `[['A','C'],['A'],[True]]`.

> Return a Python object _dict_ resuming the score, status of the taken lesson and the parent-course status whether was approved.



