import math


class PyPoint:
	"""
	PyPoint is a class used to simultaneously describe the behaviour of points (vectors) in a 2D space with
		cartesian and polar coordinates. Changing one coordinate will change the value of the others, i.e. when changing
		a cartesian coordinate the polar coordinates will be recalculated, and vice-versa.
		No methods need to be called to recalculate any of the coordinates, this is done automatically, e.g. if you set
		a new 'x' and 'r' then 'a' will be updated.
	"""

	def __init__(self, x=None, y=None, r=None, a=None):
		"""
		Create a 2D point from cartesian or polar coordinates.

		:arg x: (float || tuple || PyPoint, optional) If x is a float then y should also be a float. If x is a tuple,
		it must contain 2 digits representing x and y. If x is a PyPoint a copy of that point will be created.
		:arg y: (float, optional) y coordinate of x, y pair.
		:arg r: (float, optional) radius of polar coordinate set.
		:arg a: (float, optional) angle of polar coordinate set (in radians).
		:param x: int
		:param y: int
		:param r: int
		:param a: int
		"""
		self._x = 0.0
		self._y = 0.0
		self._r = 0.0
		self._a = 0.0

		if type(x) == PyPoint:
			# Create point using another point
			self._x = x.x
			self._y = x.y
			self._r = x.r
			self._a = x.a
		elif type(x) == tuple:
			# Create point from tuple
			self._x = x[0]
			self._y = x[1]
			self._r = math.sqrt(x[0] ** 2 + x[1] ** 2)
			self._a = math.atan2(x[1], x[0])
		elif not x == None and not y == None:
			# Create from x and y
			self._x = x
			self._y = y
			self._r = math.sqrt(x ** 2 + y ** 2)
			self._a = math.atan2(y, x)
		elif not r == None and not a == None:
			# Create from r and a
			self._r = r
			self._a = a
			self._x = r * math.cos(a)
			self._y = r * math.sin(a)

	def _calc_cartesian(self):
		self._x = self._r * math.cos(self._a)
		self._y = self._r * math.sin(self._a)

	def _calc_polar(self):
		self._r = math.sqrt(self._x ** 2 + self._y ** 2)
		self._a = math.atan2(self._y, self._x)

	def cartesian(self, x=None, y=None):
		"""
		:param self: self
		:param x: float || tuple, optional: If tuple it must contain the values for both x and y.
		:param y: float, optional
		:return: set of cartesian coordinates, if params are empty a tuple with (x, y) will be returned.
		"""
		if not x:
			return self._x, self._y
		elif type(x) == tuple:
			self._x = x[0]
			self._y = x[1]
			self._calc_polar()
		elif not x == None and not y == None:
			self._x = float(x)
			self._y = float(y)
			self._calc_polar()

	def polar(self, r=None, a=None):
		"""
		:param self: self
		:param r: float || tuple, optional: If tuple it must contain the values for both r and a.
		:param a: float, optional
		:return: set of polar coordinates, if params are empty a tuple with (r, a) will be returned.
		"""
		if not r:
			return self._r, self._a
		elif type(r) == tuple:
			self._r = r[0]
			self._a = r[1]
			self._calc_cartesian()
		elif not r == None and not a == None:
			self._r = float(r)
			self._a = float(a)
			self._calc_cartesian()

	def ints(self):
		""":return cartesian coordinates as a tuple of ints"""
		return int(self._x), int(self._y)

	@property
	def x(self):
		"""x coordinate of a cartesian pair"""
		return self._x

	@x.setter
	def x(self, val):
		self._x = float(val)
		self._calc_polar()

	@property
	def y(self):
		"""y coordinate of a cartesian pari"""
		return self._y

	@y.setter
	def x(self, val):
		self._y = float(val)
		self._calc_polar()

	@property
	def r(self):
		"""Radius value of polar coordinate"""
		return self._r

	@r.setter
	def r(self, val):
		self._r = float(val)
		self._calc_cartesian()

	@property
	def a(self):
		"""Angle value of polar coordinate"""
		return self._a

	@a.setter
	def a(self, val):
		self._a = float(val)
		self._calc_cartesian()

	def __repr__(self):
		""":return string with format 'PyPoint(x, y)(r, a)"""
		return f'PyPoint({self._x}, {self._y})({self._r}, {self._a})'

	def __add__(self, other):
		"""Vector addition"""
		return PyPoint(self._x + other.x, self._y + other.y)

	def __iadd__(self, other):
		"""Vector addition"""
		self._x += other.x
		self._y += other.y
		self._calc_polar()
		return self

	def __sub__(self, other):
		"""Vector subtraction"""
		return PyPoint(self._x - other.x, self._y - other.y)

	def __isub__(self, other):
		self._x -= other.x
		self._y -= other.y
		self._calc_polar()
		return self

	def __mul__(self, val):
		"""Scalar multiplication"""
		return PyPoint(r=self.x * val, a=self.a * val)

	def __rmul__(self, val):
		"""Scalar multiplication"""
		return PyPoint(r=self.r * val, a=self.a * val)

	def __imul__(self, val):
		"""Scalar multiplication"""
		self.r *= val
		return self
