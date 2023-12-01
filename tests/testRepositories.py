import repositories
import domain
import utils

class TestStudentRepository:

	def __init__(self):
		"""
		A function that initializes the instance of the TestStudentRepository class.
		"""
		self.__randomGenerator = utils.RandomGenerator()
	
	def testAddStudent(self):
		"""
		 A function that tests if the addStudent functions works properly.
		 Raises: AssertionError
		"""
		repository = repositories.StudentsRepository()
		#Test repo is empty
		assert len(repository) == 0
		#Test if the student was added
		id1 = self.__randomGenerator.generateId()
		name1 = self.__randomGenerator.generateString()
		group1 =  self.__randomGenerator.generateNumber()
		student1 = domain.Student(id1, name1, group1)
		repository.addStudent(student1)
		assert len(repository) == 1
		assert repository.getStudentById(student1.getId()) == student1
		#Test getting exception when adding a student with the id of an existing student
		name2 = self.__randomGenerator.generateString()
		group2 = self.__randomGenerator.generateNumber()
		student2 = domain.Student(id1, name2, group2)
		try:
			repository.addStudent(student2)
			assert False
		except Exception:
			assert True

	def testGetAllStudents(self):
		"""
		A function that checks if getAllStudents works properly.
		Raises: AssertionError
		"""
		repository = repositories.StudentsRepository()
		#Test getAllStudents returns an empty list if there are no students in repo
		assert len(repository) == 0
		#Test if 2 students were added
		id1 = self.__randomGenerator.generateId()
		name1 = self.__randomGenerator.generateString()
		group1 = self.__randomGenerator.generateNumber()
		id2 = self.__randomGenerator.generateId()
		name2 = self.__randomGenerator.generateString()
		group2 = self.__randomGenerator.generateNumber()
		student1 = domain.Student(id1, name1, group1)
		student2 = domain.Student(id2, name2, group2)
		repository.addStudent(student1)
		repository.addStudent(student2)
		assert len(repository) == 2
		students = repository.getAllStudents()
		print(students)
		#Test if the first student of the list corresponds with student1
		assert repository.getStudentById(student1.getId()) == students[0]
		#Test if the second student of the list corresponds with student2
		assert repository.getStudentById(student2.getId()) == students[1]

	def testGetStudentById(self):
		"""
		A function that checks if the getStudentById works properly.
		Raises: AssertionError
		"""
		id1 = self.__randomGenerator.generateId()
		name1 = self.__randomGenerator.generateString()
		group1 = self.__randomGenerator.generateNumber()
		id2 = self.__randomGenerator.generateId()
		name2 = self.__randomGenerator.generateString()
		group2 = self.__randomGenerator.generateNumber()
		repository = repositories.StudentsRepository()
		student1 = domain.Student(id1, name1, group1)
		student2 = domain.Student(id2, name2, group2)
		repository.addStudent(student1)
		repository.addStudent(student2)
		#Test if the function returns the right student.
		returnedStudent = repository.getStudentById(id2)
		assert returnedStudent == student2
		#Test if the function raises an exception when it is asked to return a student with an id it doesn't have.
		try:
			repository.getStudentById(self.__randomGenerator.generateId())
			assert False
		except Exception:
			assert True

	def testUpdateStudentById(self):
		"""
		A function that checks if the updateStudentById works properly.
		Raises: AssertionError
		"""
		repository = repositories.StudentsRepository()
		id1 = self.__randomGenerator.generateId()
		name1 = self.__randomGenerator.generateString()
		group1 = self.__randomGenerator.generateNumber()
		id2 = self.__randomGenerator.generateId()
		name2 = self.__randomGenerator.generateString()
		group2 = self.__randomGenerator.generateNumber()
		student1 = domain.Student(id1, name1, group1)
		student2 = domain.Student(id2, name2, group2)
		repository.addStudent(student1)
		repository.addStudent(student2)
		#Test if the correct student was updated.
		id3 = self.__randomGenerator.generateId()
		name3 = self.__randomGenerator.generateString()
		group3 = self.__randomGenerator.generateNumber()
		newStudent = domain.Student(id3, name3, group3)
		repository.updateStudentById(id1, newStudent)
		assert repository.getStudentById(newStudent.getId()) == newStudent
		#Test if the function raises an exception when it can find what student to update.
		try:
			repository.updateStudentById(self.__randomGenerator.generateId(), newStudent)
			assert False
		except Exception:
			assert True
		#Test if the function raises an error when it tries to change the id of the student to an id that already exists in the repo.
		try:
			repository.updateStudentById(id2, newStudent)
			assert False
		except Exception:
			assert True

	def testDeleteStudentById(self):
		"""
		A function that checks if the deleteStudentNyId function works properly.
		Raises: Assertion Error
		"""
		repository = repositories.StudentsRepository()
		id1 = self.__randomGenerator.generateId()
		name1 = self.__randomGenerator.generateString()
		group1 = self.__randomGenerator.generateNumber()
		id2 = self.__randomGenerator.generateId()
		name2 = self.__randomGenerator.generateString()
		group2 = self.__randomGenerator.generateNumber()
		student1 = domain.Student(id1, name1, group1)
		student2 = domain.Student(id2, name2, group2)
		repository.addStudent(student1)
		repository.addStudent(student2)
		#Test if the function deletes the correct student1
		repository.deleteStudentById(id1)
		assert len(repository) == 1
		try:
			repository.getStudentById(id2)
			assert True
		except Exception:
			assert False
		#Test if the function raises an error when you try to delete a student with an id that isn't present in the repo
		try:
			repository.deleteStudentById(self.__randomGenerator.generateId())
			assert False
		except Exception:
			assert True
		#Test if the function can delete the remaining student
		repository.deleteStudentById(id2)
		assert len(repository) == 0

class TestProblemsRepository:

	def __init__(self):
		"""
		A function that initializes the instance of the TestProblemsRepository class.
		"""
		self.__randomGenerator = utils.RandomGenerator()
		
	def testAddNewProblem(self):
		"""
		A function that tests if the addNewProblem works properly.
		Raises: Assertion Error.
		"""
		labProb1 = self.__randomGenerator.generateProblemId()
		description1 = self.__randomGenerator.generateString()
		deadline1 = self.__randomGenerator.generateRandomDate()
		description2 = self.__randomGenerator.generateString()
		deadline2 = self.__randomGenerator.generateRandomDate()
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem(labProb1, description1, deadline1)
		problem2 = domain.LaboratoryProblem(labProb1, description2, deadline2)
		#Test if the function can add the problem properly.
		assert len(repository) == 0
		repository.addNewProblem(problem1)
		assert len(repository) == 1
		assert repository.getProblemByLaboratoryNumberProblemNumber(problem1.getLaboratoryNumberProblemNumber()) == problem1
		#Test if the function raises an exception when a problem with the same combination o problem number and laboratory number is added in the repository
		try:
			repository.addNewProblem(problem2)
			assert False
		except Exception:
			assert True

	def testGetProblemByLabNumberProblemNumber(self):
		"""
		A function that tests if the getProblemByLabNumberProblemNumber functions properly.
		Raises: Assertion Error.
		"""
		labProb1 = self.__randomGenerator.generateProblemId()
		description1 = self.__randomGenerator.generateString()
		deadline1 = self.__randomGenerator.generateRandomDate()
		labProb2 = self.__randomGenerator.generateProblemId()
		description2 = self.__randomGenerator.generateString()
		deadline2 = self.__randomGenerator.generateRandomDate()
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem(labProb1, description1, deadline1)
		problem2 = domain.LaboratoryProblem(labProb2, description2, deadline2)
		repository.addNewProblem(problem1)
		repository.addNewProblem(problem2)
		#Test if the right problem is returned.
		problem = repository.getProblemByLaboratoryNumberProblemNumber(labProb2)
		assert problem == problem2
		#Test if the function raises an exception when I try to get a problem with a wrong combination of laboratory number and problem number.
		try:
			problem = repository.getProblemByLaboratoryNumberProblemNumber(self.__randomGenerator.generateProblemId())
			assert False
		except Exception:
			assert True

	def testGetAllProblems(self):
		"""
		A function that checks if the getAllProblems function works properly.
		Raises: Assertion Error
		"""
		labProb1 = self.__randomGenerator.generateProblemId()
		description1 = self.__randomGenerator.generateString()
		deadline1 = self.__randomGenerator.generateRandomDate()
		labProb2 = self.__randomGenerator.generateProblemId()
		description2 = self.__randomGenerator.generateString()
		deadline2 = self.__randomGenerator.generateRandomDate()
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem(labProb1, description1, deadline1)
		problem2 = domain.LaboratoryProblem(labProb2, description2, deadline2)
		#Test if the function can return an empty list.
		problems = repository.getAllProblems()
		assert len(problems) == 0
		#Test if the function returns the problems properly.
		repository.addNewProblem(problem1)
		repository.addNewProblem(problem2)
		problems = repository.getAllProblems()
		assert problems[0] == problem1
		assert problems[1] == problem2

	def testUpdateProblemByLabNumberProblemNumber(self):
		"""
		A function that checks if the function updateProblemByLabNumberProblemNumber functions properly.
		Raises: Assertion Error
		"""
		labProb1 = self.__randomGenerator.generateProblemId()
		description1 = self.__randomGenerator.generateString()
		deadline1 = self.__randomGenerator.generateRandomDate()
		labProb2 = self.__randomGenerator.generateProblemId()
		description2 = self.__randomGenerator.generateString()
		deadline2 = self.__randomGenerator.generateRandomDate()
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem(labProb1, description1, deadline1)
		problem2 = domain.LaboratoryProblem(labProb2, description2, deadline2)
		repository.addNewProblem(problem1)
		repository.addNewProblem(problem2)
		#Test if the right problem is updated
		labProb3 = self.__randomGenerator.generateProblemId()
		description3 = self.__randomGenerator.generateString()
		deadline3 = self.__randomGenerator.generateRandomDate()
		newProblem = domain.LaboratoryProblem(labProb3, description3, deadline3)
		repository.updateProblemByLaboratoryNumberProblemNumber(labProb2, newProblem)
		assert repository.getProblemByLaboratoryNumberProblemNumber(labProb3) == newProblem
		#Test if the function raises an exception when a combination of laboratory number and problem number that do not exist is input.
		try:
			repository.updateProblemByLaboratoryNumberProblemNumber(self.__randomGenerator.generateProblemId(), newProblem)
			assert False
		except Exception:
			assert True
		#Test if the function raises an exception when the new combination of laboratory number and problem number coincides with the combination of another problem.
		description4 = self.__randomGenerator.generateString()
		deadline4 = self.__randomGenerator.generateRandomDate()
		anotherNewProblem = domain.LaboratoryProblem(labProb1, description4, deadline4)
		try:
			repository.updateProblemByLaboratoryNumberProblemNumber(labProb3, anotherNewProblem)
			assert False
		except Exception:
			assert True

	def testDeleteProblemByLabNumberProblemNumber(self):
		"""
		A function that tests if deleteProblemByLabNumberProblemNumber works properly.
		Raises: Assertion Error
		"""
		labProb1 = self.__randomGenerator.generateProblemId()
		description1 = self.__randomGenerator.generateString()
		deadline1 = self.__randomGenerator.generateRandomDate()
		labProb2 = self.__randomGenerator.generateProblemId()
		description2 = self.__randomGenerator.generateString()
		deadline2 = self.__randomGenerator.generateRandomDate()
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem(labProb1, description1, deadline1)
		problem2 = domain.LaboratoryProblem(labProb2, description2, deadline2)
		repository.addNewProblem(problem1)
		repository.addNewProblem(problem2)
		#Test deleting the right problem.
		repository.deleteProblemByLaboratoryNumberProblemNumber(labProb1)
		problems = repository.getAllProblems()
		assert problems[0] == problem2
		#Test function raising an exception when the input combination of laboratory number and problem number isn't present in the repository.
		try:
			repository.deleteProblemByLaboratoryNumberProblemNumber(labProb1)
			assert False
		except Exception:
			assert True

