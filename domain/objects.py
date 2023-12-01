class Student:

	def __init__(self, id, name, group):
		"""
		A function that initializes the class when it is created (Constructor)
		Preconditions: id: a positive integer
									 name: a string
									 group: a positive integer
		Post-conditions: -
		"""
		self.__id = id
		self.__name = name
		self.__group = group

	def __eq__(self, otherStudent):
		"""
		A function that overwrites the equality operator in order to be able the compare 2 students.
		Precondition: otherStudent: a instance of the student class
		Post-conditions: A bool
		"""
		if self.__id != otherStudent.getId() or self.__name != otherStudent.getName() or self.__group != otherStudent.getGroup():
			return False
		return True
	
	def getId(self):
		"""
		A function that returns the id of the student
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return self.__id

	def getName(self):
		"""
		A function that returns the name of the student
		Preconditions: -
		Post-conditions: a string
		"""
		return self.__name

	def getGroup(self):
		"""
		A function that returns the group of the student
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return self.__group

	def setId(self, newId):
		"""
		A function that sets the id of the student to newId.
		Preconditions: newId: a positive integer
		Post-conditions: -
		"""
		self.__id = newId

	def setName(self, newName):
		"""
		A function that sets the name of the student to newName
		Preconditions: newName: a string
		Post-conditions: -
		"""
		self.__name = newName

	def setGroup(self, newGroup):
		"""
		A function that sets the group of the student to newGroup
		Preconditions: newName: an integer
		Post-conditions: -
		"""
		self.__group = newGroup

class LaboratoryProblem:

	def __init__(self, laboratoryNumberProblemNumber, description, deadline):
		"""
		A function that initializes the current instance of the laboratoryProblem class (Constructor).
		Preconditions: a string with the following format: laboratoryNumber_problemNumber
									 description: a string
									 deadline: a string with the following format: mm/dd/yyyy 
		"""
		self.__laboratoryNumberProblemNumber = laboratoryNumberProblemNumber
		self.__description = description
		self.__deadline = deadline

	def __eq__(self, otherLaboratoryProblem):
		"""
		A function that overwrites the equality operator in order to compare instances of LaboratoryProblem.
		Preconditions: otherLaboratoryProblem: instance of the LaboratoryProblem class
		Post-conditions: a bool
		"""
		if self.__laboratoryNumberProblemNumber != otherLaboratoryProblem.getLaboratoryNumberProblemNumber():
			return False
		if self.__description != otherLaboratoryProblem.getDescription():
			return False
		if self.__deadline != otherLaboratoryProblem.getDeadline():
			return False
		return True

	def getLaboratoryNumberProblemNumber(self):
		"""
		A function that returns the laboratory number and problem number of the problem.
		Preconditions: self: -
		Post-conditions: a string
		"""
		return self.__laboratoryNumberProblemNumber

	def getDescription(self):
		"""
		A function that returns the description of the problem.
		Preconditions: -
		Post-conditions: a string
		"""
		return self.__description

	def getDeadline(self):
		"""
		A function that returns the deadline of the problem.
		Preconditions: -
		Post-conditions: a string with the following format: mm/dd/yyyy where mm is a positive integer between 1 and 12, dd is a positive integer between 1 and 31 and yyyy is a positive integer
		"""
		return self.__deadline

	def setLaboratoryNumberProblemNumber(self, newLaboratoryNumberProblemNumber):
		"""
		A function that sets the number of the laboratory to newLaboratoryNumberProblemNumber
		Preconditions: newLaboratoryNumberProblemNumber: a string with the following format: laboratoryNumber_problemNumber
		Post-conditions: -
		"""
		self.__laboratoryNumberProblemNumber = newLaboratoryNumberProblemNumber

	def setDescription(self, newDescription):
		"""
		A function that sets the description of the problem to newDescription.
		Preconditions: newDescription: a string
		Post-conditions: -
		"""
		self.__description = newDescription

	def setDeadline(self, newDeadline):
		"""
		A function that sets the deadline of the problem to newDeadline.
		Preconditions: newDeadline: a string that has the following format: mm/dd/yyyy where mm is a positive integer between 1 and 12, dd is a positive integer between 1 and 31 and yyyy is a positive integer.
		Post-conditions: -
		"""
		self.__deadline = newDeadline