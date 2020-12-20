class Animal():
	__name = None
	__age = None
	def __init__(self, name_and_age):
		self.__name, self.__age = name_and_age.split()
	def gAge(self):
		return self.__age
	def gName(self):
		return self.__name
	def __str__(self):
		return self.get_str()

class Zebra(Animal):
	__type = 'Zebra'
	def get_str(self):
		return ('Type of animal: ' + self.__type + '; Name: ' + self.gName() + '; Age: ' + self.gAge())

class Dolphin(Animal):
	__type = 'Dolphin'
	def get_str(self):
		return ('Type of animal: ' + self.__type + '; Name: ' + self.gName() + '; Age: ' + self.gAge())

if __name__ == "__main__" :
	print("Enter Name and Age of Zebra:")
	zebr = Tiger(input())
	print("Enter Name and Age of Dolphin:")	
	dolph = Dolphin(input())

	print(zebr)
	print(dolph)


