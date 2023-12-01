import domain
import utils

class TestObjects:
	
	def __init__(self):
		"""
		A function that initializes the instance of the TestObjects class.
		"""
		self.__randomGenerator = utils.RandomGenerator()

	def testStudent(self):
		"""
		A function that checks if the student class works properly.
		Raises: Assertion Error
		"""
		id = self.__randomGenerator.generateId()
		name = self.__randomGenerator.generateString()
		group = self.__randomGenerator.generateNumber()
		student1 = domain.Student(id, name, group)
		
		#Test getters.
		assert student1.getId() == id
		assert student1.getName() == name
		assert student1.getGroup() == group
		
		#Test setters.
		newId = self.__randomGenerator.generateId()
		newName = self.__randomGenerator.generateString()
		newGroup = self.__randomGenerator.generateNumber()
		student1.setId(newId)
		student1.setName(newName)
		student1.setGroup(newGroup)
		assert student1.getId() == newId
		assert student1.getName() == newName
		assert student1.getGroup() == newGroup
		
		#Test overwritten equality operator.
		student2 = domain.Student(id, name, group)
		student3 = domain.Student(id, name, group)
		assert student1 != student2
		assert student2 == student3

	def testLaboratoryProblem(self):
		"""
		A function that checks if the LaboratoryProblem class works properly.
		Raises: Assertion Error.
		"""
		laboratoryNumberProblemNumber = self.__randomGenerator.generateProblemId()
		description = self.__randomGenerator.generateString()
		deadline = self.__randomGenerator.generateRandomDate()
		problem1 = domain.LaboratoryProblem(laboratoryNumberProblemNumber, description, deadline)

		#Test getters
		assert laboratoryNumberProblemNumber == problem1.getLaboratoryNumberProblemNumber()
		assert description == problem1.getDescription()
		assert deadline == problem1.getDeadline()
		
		#Test setters
		newlaboratoryNumberProblemNumber = self.__randomGenerator.generateProblemId()
		newDescription = self.__randomGenerator.generateString()
		newDeadline = self.__randomGenerator.generateRandomDate()
		problem1.setLaboratoryNumberProblemNumber(newlaboratoryNumberProblemNumber)
		problem1.setDescription(newDescription)
		problem1.setDeadline(newDeadline)
		assert newlaboratoryNumberProblemNumber == problem1.getLaboratoryNumberProblemNumber()
		assert newDescription == problem1.getDescription()
		assert newDeadline == problem1.getDeadline()
		
		#Test overwritten equality operator.
		problem2 = domain.LaboratoryProblem(laboratoryNumberProblemNumber, description, deadline)
		problem3 = domain.LaboratoryProblem(laboratoryNumberProblemNumber, description, deadline)
		assert problem1 != problem2
		assert problem2 == problem3
