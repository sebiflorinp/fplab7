import utils

class StudentValidator:

	def validateStudent(self, student):
		"""
		A function that checks if an instance of the student class is valid.
		Preconditions: student: an instance of the Student class
		Post-conditions: -
		Raises: InvalidStudentError: id is not a positive integer.
																 id is empty.
																 name is empty.
																 group is not a positive integer.
																 group is empty.
		"""
		errors = []
		#Check if the entered id is valid
		try:
			int(student.getId())
			if int(student.getId()) < 0:
				assert False
		except ValueError and AssertionError:
			errors.append("id is not a positive integer.")
		if student.getId() == "":
			errors.append("id is empty.")
		#Check if the entered name is valid
		if student.getName() == "":
			errors.append("name is empty.")
		#Check if the entered group is valid
		try:
			int(student.getGroup())
			if int(student.getGroup()) < 0:
				assert False
		except ValueError:
			errors.append("group is not a positive integer.")
		except AssertionError:
			errors.append("group is not a positive integer.")
		if student.getGroup() == "":
			errors.append("group is empty.")
		#Raise InvalidStudentError if any field is invalid
		if len(errors):
			raise utils.InvalidStudentError(errors)

class ProblemValidator:

	def validateProblem(self, problem):
		"""
		A function that checks if a laboratory problem is valid.
		Preconditions: problem: an instance of the LaboratoryProblem class
		Post-conditions: -
		Raises: InvalidProblemError: laboratoryNumberProblemNumber does not respect the following format: laboratoryNumber_problemNumber
																 laboratoryNumber is not a positive integer.
																 laboratoryNumber is empty.
																 problemNumber is not a positive integer.
																 problemNumber is empty.
																 description is empty.
																 deadline does not respect the following format: mm/dd/yyyy.
																 deadline month is not a positive integer between 1 and 12.
																 deadline day is not a positive integer between 1 and 31.
																 deadline year is not a positive integer.
																 deadline month, day or year is empty.
		"""
		errors = []
		#Check if laboratoryNumberProblemNumber is valid
		if len(problem.getLaboratoryNumberProblemNumber().split("_")) != 2:
			errors.append("laboratoryNumberProblemNumber does not respect the following format: laboratoryNumber_problemNumber")
		else:
			#Check if problemNumber is valid
			laboratoryNumber = problem.getLaboratoryNumberProblemNumber().split("_")[0]
			try:
				int(laboratoryNumber)
				if int(laboratoryNumber) < 0:
					raise Exception
			except ValueError:
				errors.append("laboratoryNumber is not a positive integer.")
			except Exception:
				errors.append("laboratoryNumber is not a positive integer.")
			if laboratoryNumber == "":
				errors.append("laboratoryNumber is empty.")
			#Check if problemNumber is valid
			problemNumber = problem.getLaboratoryNumberProblemNumber().split("_")[1]
			try:
				int(problemNumber)
				if int(problemNumber) < 0:
					raise Exception
			except ValueError:
				errors.append("problemNumber is not a positive integer.")
			except Exception:
				errors.append("problemNumber is not a positive integer.")
			else:
				if int(problemNumber) < 0:
					errors.append("problemNumber is empty.")
		#Check if description is valid
		if len(problem.getDescription()) == 0:
			errors.append("description is empty.")
		#Check if deadline is valid
		date = problem.getDeadline()
		date = date.split("/")
		if len(date) != 3:
			errors.append("deadline does not respect the following format: mm/dd/yyyy.")
		else:
			#Check if the month of deadline is valid
			try:
				int(date[0])
				if not 1 <= int(date[0]) <= 12:
					raise Exception
			except ValueError:
				errors.append("deadline month is not a positive integer between 1 and 12.")
			except Exception:
				errors.append("deadline month is not a positive integer between 1 and 12.")
			#Check if the day of deadline is valid
			try:
				int(date[1])
				if not 1 <= int(date[1]) <= 31:
					raise Exception
			except ValueError:
				errors.append("deadline day is not a positive integer between 1 and 31.")
			except Exception:
				errors.append("deadline day is not a positive integer between 1 and 31.")
			#Check if the year of the deadline is valid
			try:
				int(date[2])
				if int(date[2]) < 0:
					raise Exception
			except ValueError:
				errors.append("deadline year is not a positive integer.")
			except Exception:
				errors.append("deadline year is not a positive integer.")
			#Check if the year, month or day is empty
			if date[0] == "" or date[1] == "" or date[2] == "":
				errors.append("deadline month, day or year is empty.")
		if len(errors):
			raise utils.InvalidProblemError(errors)