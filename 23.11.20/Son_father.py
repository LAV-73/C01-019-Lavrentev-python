class People():
	__r = None
	__n = None
	def get_Name(self):
		return self.__n
	def __str__(self):
		return self.push()
	def get_Relation(self):
		return self.__r
	def __init__(self, role, name):
		self.__r = role
		self.__n = name
class Son(People):
	def push(self):
		return "Relationship: " + self.get_Relation() + "  Name: " + self.get_Name()
class Father(People):
	def push(self):
		return "Relationship: " + self.get_Relation() + "  Name: " + self.get_Name()
if __name__ == "__main__" :
	poppa = Father('Father', input())
	sonny = Son('Son', input())
	print(poppa)
	print(sonny)
