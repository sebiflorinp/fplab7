from tests.testObjects import TestObjects
from tests.testValidators import TestValidators
from tests.testRepositories import TestProblemsRepository, TestStudentRepository

class RunAllTests:

	def runAllTests(self):
		"""
		A function that runs all tests.
		Preconditions: -
		Post-conditions: -
		"""
		#Run object tests.
		objectsTests = TestObjects()
		objectsTests.testStudent()
		objectsTests.testLaboratoryProblem()
		
		#Run validator tests.
		validatorsTests = TestValidators()
		validatorsTests.testStudentValidator()
		validatorsTests.testProblemValidator()

		#Run students repo tests
		studentsRepositoryTests = TestStudentRepository()
		studentsRepositoryTests.testAddStudent()
		studentsRepositoryTests.testGetStudentById()
		studentsRepositoryTests.testGetAllStudents()
		studentsRepositoryTests.testUpdateStudentById()
		studentsRepositoryTests.testDeleteStudentById()

		#Run problems repo tests
		problemsRepositoryTests = TestProblemsRepository()
		problemsRepositoryTests.testAddNewProblem()
		problemsRepositoryTests.testGetProblemByLabNumberProblemNumber()
		problemsRepositoryTests.testGetAllProblems()
		problemsRepositoryTests.testUpdateProblemByLabNumberProblemNumber()
		problemsRepositoryTests.testDeleteProblemByLabNumberProblemNumber()

