import domain
import utils

class TestValidators:

	def testStudentValidator(self):
		"""
		A function that tests the student validator.
		Preconditions: -
		Post-conditions: -
		Raises: Assertion Error
		"""
		#Prepare the needed data to test studentValidator.
		student1 = domain.Student(1, "Ion", 201)
		student2 = domain.Student("", "", "rer43")
		student3 = domain.Student("fd","George", -1)
		student4 = domain.Student(2, "Ionescu", 213)
		#Test studentValidator
		studentValidator = domain.StudentValidator()
		try:
			studentValidator.validateStudent(student1)
			assert False
		except AssertionError:
			assert True
		try:
			studentValidator.validateStudent(student2)
			assert False
		except ValueError:
			assert True
		try:
			studentValidator.validateStudent(student3)
			assert False
		except ValueError:
			assert True
		try:
			studentValidator.validateStudent(student4)
			assert False
		except AssertionError:
			assert True

	def testProblemValidator(self):
		"""
		A function that tests ProblemValidator.
		Preconditions: -
		Post-conditions: -
		Raises: Assertion Error
		"""
		#Prepare data for testing problemValidator
		problem1 = domain.LaboratoryProblem("1_1", "A difficult problem.", "12/10/2023")
		problem2 = domain.LaboratoryProblem("1_2", "", "12/10/2023")
		problem3 = domain.LaboratoryProblem("dfds_dsds1", "A difficult problem.", "1a/-10/2023")
		problem4 = domain.LaboratoryProblem("2fdsfds", "A difficult problem.", "12.10.2023")
		#Test problemValidator
		problemValidator = domain.ProblemValidator()
		try:
			problemValidator.validateProblem(problem1)
			assert False
		except AssertionError:
			assert True
		try:
			problemValidator.validateProblem(problem2)
			assert False
		except utils.InvalidProblemError:
			assert True
		try:
			problemValidator.validateProblem(problem3)
			assert False
		except utils.InvalidProblemError:
			assert True
		try:
			problemValidator.validateProblem(problem4)
			assert False
		except utils.InvalidProblemError:
			assert True