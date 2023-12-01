import random

class RandomGenerator:
	def __init__(self):
		"""
		A function that initializes the current instance of RandomGenerator.
		"""
		self.__ids = []
		self.__problemIds = []
		self.__days = []
		self.__months = []
		for id in range(1, 10000):
			self.__ids.append(id)
		for laboratoryNumber in range(1, 101):
			for problemNumber in range(1, 1001):
				self.__problemIds.append(str(laboratoryNumber) + "_" + str(problemNumber))
		for day in range(1, 32):
			self.__days.append(day)
		for month in range(1, 13):
			self.__months.append(month)
		random.seed(2)

	def generateId(self):
		"""
		A function that generates a random id.
		Preconditions: -
		Post-conditions: a random integer between 0 and 9999.
		Raises: Exception: There are no ids left.
		"""
		try:
			randomId = random.choice(self.__ids)
			self.__ids.remove(randomId)
		except:
			raise Exception("There are no ids left.")
		return randomId
	
	def generateProblemId(self):
		"""
		A function that generates a random id for lab problems.
		Preconditions: -
		Post-conditions: a string with the following format: laboratoryNumber_problemNumber
		Raises: Exception: There are no ids left.
		"""
		try:
			randomId = random.choice(self.__ids)
			self.__ids.remove(randomId)
		except:
			raise Exception("There are no ids left.")
		return randomId
	
	def generateString(self):
		"""
		A function that generates a random string of a random length.
		Preconditions: -
		Post-conditions: a random string with a length between 1 and 100.
		"""
		characters = []
		for character in range(ord('a'), ord('z')):
			characters.append(chr(character))
		for character in range(ord('A'), ord('Z')):
			characters.append(chr(character))
		length = 0
		while True:
			length = int(random.random() * 100)
			if length != 0:
				break
		word = ""
		for index in range(0, length):
			word += random.choice(characters)
		return word
	
	def generateRandomDate(self):
		"""
		A function that generates a random date with the following format: mm/dd/yyyy.
		Preconditions: -
		Post-conditions: a string with the following format: mm/dd/yyyy
		"""
		return str(random.choice(self.__months)) + "/" + str(random.choice(self.__days)) + "/" + str(random.random() * 10000)
	
	def generateNumber(self):
		"""
		A function that generates a random number.
		Preconditions: -
		Post-conditions: a random positive integer.
		"""
		return int(random.random() * 10000)
	