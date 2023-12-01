import utils

class StudentsRepository:

	def __init__(self):
		"""
		A function that initializes the current class instance (constructor).
		Preconditions: -
		Post-conditions: -
		"""
		self.__students = {}

	def __len__(self):
		"""
		A function that overrites the len method and returns the length of the list of students.
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return len(self.__students)

	def addStudent(self, student):
		"""
		A function that adds a student to the current list of students]
		Preconditions: student: a student object
		Post-conditions: -
		Raises: StudentRepositoryProblem: There is already a student with the id of the input student.
		"""
		if student.getId() in self.__students:
			raise utils.StudentRepositoryError("There is already a student with the id of the input student.")
		self.__students[student.getId()] = student

	def getStudentById(self, studentId):
		"""
		A function that return a student with the id of studentId.
		Preconditions: studentId: a positive integer
		Post-conditions: an instance of the student class
		Raises: StudentRepositoryProblem: There is no student with the selected id.
		"""
		if studentId not in self.__students:
			raise utils.StudentRepositoryError("There is no student with the selected id.")
		return self.__students[studentId]

	def getAllStudents(self):
		"""
		A function that returns all students from the list of students.
		Preconditions: -
		Post-conditions: a list of instances of the Student class.
		"""
		students = []
		for key in self.__students:
			students.append(self.__students[key])
		return students

	def updateStudentById(self, studentId, newStudent):
		"""
		A function that updates the student with the id of studentID.
		Preconditions: studentId: a positive integer
									 newStudent: an object of student type
		Post-conditions: -
		Raises: StudentRepositoryProblem: There is no student with the input id.
											                There is already another student with the newId.
		"""
		if studentId not in self.__students:
			raise utils.StudentRepositoryError("There is no student with the input id.")
		if newStudent.getId() in self.__students and newStudent.getId() != studentId:
			raise utils.StudentRepositoryError("There is already another student with the newId.")
		del self.__students[studentId]
		self.__students[newStudent.getId()] = newStudent

	def deleteStudentById(self, studentId):
		"""
		A function that deletes from the list of students the student with the id of studentId.
		Preconditions: studentId: positive integer
		Post-conditions: -
		Raises: StudentRepositoryProblem: There is no student with the input id.
		"""
		if studentId not in self.__students:
			raise utils.StudentRepositoryError("There is no student with the input id.")
		del self.__students[studentId]

class ProblemsRepository:

	def __init__(self):
		"""
		The constructor of the function, initializes the list of problems.
		Preconditions: -
		Post-conditions: -
		"""
		self.__problems = {}

	def __len__(self):
		"""
		A function that overwrites the len function of the object and returns the length of the list of problems.
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return len(self.__problems)

	def addNewProblem(self, problem):
		"""
		A function that adds a new problem to the list of problems.
		Preconditions: problem: a problem type object
		Post-conditions: -
		Raises: ProblemRepositoryError: There already is a problem with the input laboratoryNumberProblemNumber.
		"""
		if problem.getLaboratoryNumberProblemNumber() in self.__problems:
			raise utils.ProblemRepositoryError("There already is a problem with the input laboratoryNumberProblemNumber.")
		self.__problems[problem.getLaboratoryNumberProblemNumber()] = problem

	def getProblemByLaboratoryNumberProblemNumber(self, laboratoryNumberProblemNumber):
		"""
		A function that returns a problem that has the problem number and the laboratory number equal to the input ones.
		Preconditions: laboratoryNumberProblemNumber: a string with the following format: laboratoryNumber_problemNumber
		Post-conditions: an object of the problem type
		Raises: ProblemRepositoryError: There is no problem with the input laboratoryNumberProblemNumber.
		"""
		if laboratoryNumberProblemNumber not in self.__problems:
			raise utils.ProblemRepositoryError("There is no problem with the input laboratoryNumberProblemNumber.")
		return self.__problems[laboratoryNumberProblemNumber]

	def getAllProblems(self):
		"""
		A function that returns all the problems in the problem repository.
		Preconditions: -
		Post-conditions: A list with all the problems present in the repository.
		"""
		problems = []
		for key in self.__problems:
			problems.append(self.__problems[key])
		return problems

	def updateProblemByLaboratoryNumberProblemNumber(self, laboratoryNumberProblemNumber, newProblem):
		"""
		A function that updates the problem that has the input laboratory number and problem number.
		Preconditions: laboratoryNumberProblemNumber: a string
									 newProblem: an object of laboratoryProblem type
		Post-conditions: -
		Raises: ProblemRepositoryError: There is no problem with the input laboratoryNumberProblemNumber.
																		There is already another problem with the input laboratoryNumberProblemNumber.
		"""
		if laboratoryNumberProblemNumber not in self.__problems:
			raise utils.StudentRepositoryError("There is no problem with the input laboratoryNumberProblemNumber.")
		if (newProblem.getLaboratoryNumberProblemNumber() in self.__problems and newProblem.getLaboratoryNumberProblemNumer() != laboratoryNumberProblemNumber):
			raise utils.StudentRepositoryError("There is already another problem with the input laboratoryNumberProblemNumber.")
		del self.__problems[laboratoryNumberProblemNumber]
		self.__problems[newProblem.getLaboratoryNumberProblemNumber()] = newProblem

	def deleteProblemByLaboratoryNumberProblemNumber(self, laboratoryNumberProblemNumber):
		"""
		A function that deletes the problem that has the input combination of laboratoryNumber and problemNumber.
		Preconditions: laboratoryNumberProblemNumber: a string
		Post-conditions: -
		Raises: ProblemRepositoryError: There is no student with the input laboratoryNumberProblemNumber.
		"""
		if laboratoryNumberProblemNumber not in self.__problems:
			raise utils.ProblemRepositoryError("There is no student with the input combination of laboratoryNumber, problemNumber.")
		del self.__problems[laboratoryNumberProblemNumber]