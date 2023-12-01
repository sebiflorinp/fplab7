import repositories
import domain

class TestStudentRepository:

	def testAddStudent(self):
		"""
		 A function that tests if the addStudent functions works properly.
		 Raises: AssertionError
		"""
		repository = repositories.StudentsRepository()
		#Test repo is empty
		assert len(repository) == 0
		#Test if the student was added
		student1 = domain.Student(1, "Ionescu", 201)
		repository.addStudent(student1)
		assert len(repository) == 1
		assert repository.getStudentById(student1.getId()) == student1
		#Test getting exception when adding a student with the id of an existing student
		student2 = domain.Student(1, "Andrei", 203)
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
		student1 = domain.Student(1, "Ionescu", 203)
		student2 = domain.Student(2, "Georgescu", 204)
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
		repository = repositories.StudentsRepository()
		student1 = domain.Student(1, "Enescu", 201)
		student2 = domain.Student(2, "Averescu", 203)
		repository.addStudent(student1)
		repository.addStudent(student2)
		#Test if the function returns the right student.
		returnedStudent = repository.getStudentById(2)
		assert returnedStudent == student2
		#Test if the function raises an exception when it is asked to return a student with an id it doesn't have.
		try:
			repository.getStudentById(3)
			assert False
		except Exception:
			assert True

	def testUpdateStudentById(self):
		"""
		A function that checks if the updateStudentById works properly.
		Raises: AssertionError
		"""
		repository = repositories.StudentsRepository()
		student1 = domain.Student(1, "Petrescu", 202)
		student2 = domain.Student(2, "Popescu", 205)
		repository.addStudent(student1)
		repository.addStudent(student2)
		#Test if the correct student was updated.
		newStudent = domain.Student(3, "Ionescu", 207)
		repository.updateStudentById(1, newStudent)
		assert repository.getStudentById(newStudent.getId()) == newStudent
		#Test if the function raises an exception when it can find what student to update.
		try:
			repository.updateStudentById(100, newStudent)
			assert False
		except Exception:
			assert True
		#Test if the function raises an error when it tries to change the id of the student to an id that already exists in the repo.
		try:
			repository.updateStudentById(2, newStudent)
			assert False
		except Exception:
			assert True

	def testDeleteStudentById(self):
		"""
		A function that checks if the deleteStudentNyId function works properly.
		Raises: Assertion Error
		"""
		repository = repositories.StudentsRepository()
		student1 = domain.Student(1, "Ionel", 201)
		student2 = domain.Student(2, "Cristi", 203)
		repository.addStudent(student1)
		repository.addStudent(student2)
		#Test if the function deletes the correct student1
		repository.deleteStudentById(1)
		assert len(repository) == 1
		try:
			repository.getStudentById(2)
			assert True
		except Exception:
			assert False
		#Test if the function raises an error when you try to delete a student with an id that isn't present in the repo
		try:
			repository.deleteStudentById(3)
			assert False
		except Exception:
			assert True
		#Test if the function can delete the remaining student
		repository.deleteStudentById(2)
		assert len(repository) == 0

class TestProblemsRepository:

	def testAddNewProblem(self):
		"""
		A function that tests if the addNewProblem works properly.
		Raises: Assertion Error.
		"""
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem("1_1", "An easy problem.", "10/30/2023")
		problem2 = domain.LaboratoryProblem("1_1", "A mind breaking problem.", "12/12/2023")
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
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem("1_1", "An easy one.", "8/22/2021")
		problem2 = domain.LaboratoryProblem("2_1", "A warm up problem.", "12/12/2012")
		repository.addNewProblem(problem1)
		repository.addNewProblem(problem2)
		#Test if the right problem is returned.
		problem = repository.getProblemByLaboratoryNumberProblemNumber("2_1")
		assert problem == problem2
		#Test if the function raises an exception when I try to get a problem with a wrong combination of laboratory number and problem number.
		try:
			problem = repository.getProblemByLaboratoryNumberProblemNumber("2_2")
			assert False
		except Exception:
			assert True

	def testGetAllProblems(self):
		"""
		A function that checks if the getAllProblems function works properly.
		Raises: Assertion Error
		"""
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem("1_1", "An easy problem.", "10/10/2022")
		problem2 = domain.LaboratoryProblem("1_2", "Another easy problem.", "10/11/2023")
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
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem("1_1", "An easy problem.", "10/10/2022")
		problem2 = domain.LaboratoryProblem("1_2", "A more difficult problem.", "10/10/2022")
		repository.addNewProblem(problem1)
		repository.addNewProblem(problem2)
		#Test if the right problem is updated
		newProblem = domain.LaboratoryProblem("2_1", "A warm up problem.", "12/23/2023")
		repository.updateProblemByLaboratoryNumberProblemNumber("1_2", newProblem)
		assert repository.getProblemByLaboratoryNumberProblemNumber("2_1") == newProblem
		#Test if the function raises an exception when a combination of laboratory number and problem number that do not exist is input.
		try:
			repository.updateProblemByLaboratoryNumberProblemNumber("10_10", newProblem)
			assert False
		except Exception:
			assert True
		#Test if the function raises an exception when the new combination of laboratory number and problem number coincides with the combination of another problem.
		anotherNewProblem = domain.LaboratoryProblem("1_1", "Another problem.", "1/1/2001")
		try:
			repository.updateProblemByLaboratoryNumberProblemNumber("2_1", anotherNewProblem)
			assert False
		except Exception:
			assert True

	def testDeleteProblemByLabNumberProblemNumber(self):
		"""
		A function that tests if deleteProblemByLabNumberProblemNumber works properly.
		Raises: Assertion Error
		"""
		repository = repositories.ProblemsRepository()
		problem1 = domain.LaboratoryProblem("1_1", "An easy problem.", "10/10/2022")
		problem2 = domain.LaboratoryProblem("1_2", "Another easy problem.", "10/10/2022")
		repository.addNewProblem(problem1)
		repository.addNewProblem(problem2)
		#Test deleting the right problem.
		repository.deleteProblemByLaboratoryNumberProblemNumber("1_1")
		problems = repository.getAllProblems()
		assert problems[0] == problem2
		#Test function raising an exception when the input combination of laboratory number and problem number isn't present in the repository.
		try:
			repository.deleteProblemByLaboratoryNumberProblemNumber("1_1")
			assert False
		except Exception:
			assert True

