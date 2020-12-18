class Shape():
	__len = None
	__heig = None
	def get_Length(self):
		return self.__len
	def get_Height(self):
		return self.__heig
	def get_Dimension(self):
		self.__len, self.__heig = list(map(float, input().split()))
class Ellips(Shape):
	def area(self):
		return 3.141592 * self.get_Length() * self.get_Height() / 4
class Triangle(Shape):
	def area(self):
		return self.get_Length() * self.get_Height() / 2
class Rectangle(Shape):
	def area(self):
		return self.get_Length() * self.get_Height()
if __name__ == '__main__':
	tria = Triangle()
	rec = Rectangle()
	ell = Ellips()
	tria.get_Dimension()
	rec.get_Dimension()
	ell.get_Dimension()
	print("Area of triangle: ", round(tria.area(), 2))
	print("Area of rectangle: ", round(rec.area(), 2))
	print("Area of ellips: ", round(ell.area(), 2))