import numpy as np

class Dual(object):

	def __init__(self, val, der=1.0):
		"""The constructor for Dual class

		Args
		======
		val: real number or an array, the value of the variable.
		der: real number or an array, the derivative of the variable. Default is 1.0. 
			Should either be 1 or has the same length as val.

		"""
		self.val = val
		try:
			n = len(self.val)
			self.val = np.array(val)
			self.der = np.array(der)
			if n == 1:
				self.der = np.array(der).reshape(1)
				return
			try:
				m = len(der)
				if m!=n:
					raise ValueError("der should either be 1 or has the same length as val")
			except TypeError:
				if der == 1:
					self.der = np.ones(n)
				else:
					raise ValueError("der should either be 1 or has the same length as val")	
		except TypeError:
			self.der = der

	def __repr__(self):
		return "{val:" + str(self.val)+ ", der:" +str(self.der)+ "}"
	
	def __pos__(self):
		"""Returns + self as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, after '+'.

		    RETURNS
		    ========
		    + self as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(-4.0)
		    >>> y = + x
		    >>> print(y.val, y.der)
		    -4.0 1.0

		"""

		val = self.val
		der = self.der
		return Dual(val, der)

	def __neg__(self):
		"""Returns - self as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, after '-'.

		    RETURNS
		    ========
		    - self as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(-4.0)
		    >>> y = - x
		    >>> print(y.val, y.der)
		    4.0 -1.0

		"""

		val = -self.val
		der = -self.der
		return Dual(val, der)

	def __eq__(self,other):
		"""Returns 'self == other' result.

		    INPUTS
		    =======
		    self: recent Dual or real number, before '=='.
		    other: recent Dual or real number, after '=='.

		    RETURNS
		    ========
		    comparison result: boolean.

		    EXAMPLES
		    =========
		    >>> x = Dual(-4,2)
		    >>> y = Dual(-4,2)
		    >>> x == y
		    True

		"""
		try:
			return (self.val == other.val) and (self.der == other.der)
		except ValueError:
			return (self.val == other.val).all() and (self.der == other.der).all()
		except AttributeError:
			return False

	def __ne__(self, other):
		"""Returns 'self != other' result.

		    INPUTS
		    =======
		    self: recent Dual or real number, before '!='.
		    other: recent Dual or real number, after '!='.

		    RETURNS
		    ========
		    comparison result: boolean.

		    EXAMPLES
		    =========
		    >>> x = Dual(-4,1)
		    >>> y = Dual(1,2)
		    >>> x != y
		    True

		"""

		try:
			return (self.val != other.val) or (self.der != other.der)
		except ValueError:
			return (self.val != other.val).any() or (self.der != other.der).any()
		except AttributeError:
			return True

	def __add__(self, other):
		"""Returns self + other as a Dual.
    
		    INPUTS
		    =======
		    self: recent Dual, before '+'.
		    other: a Dual or a real number, after '+'.

		    RETURNS
		    ========
		    self + other as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(4.0)
		    >>> y = x + Dual(2.0, der=2.0)
		    >>> print(y.val, y.der)
		    6.0 3.0

		"""

		try:
			val = self.val + other.val
			der = self.der + other.der
		except AttributeError:
			val = self.val + other
			der = self.der
		return Dual(val, der)

	def __radd__(self, other):
		"""Returns other + self as a Dual.
    
		    INPUTS
		    =======
		    self: recent Dual, after '+'.
		    other: a Dual or a real number, before '+'.

		    RETURNS
		    ========
		    other + self as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(4.0)
		    >>> y = 1.0 + x
		    >>> print(y.val, y.der)
		    5.0 1.0

	    """

		return self.__add__(other)

	

	def __sub__(self, other):
		"""Returns self - other as a Dual.

	            INPUTS
		    =======
		    self: recent Dual, before '-'.
		    other: a Dual or a real number, after '-'.

		    RETURNS
		    ========
		    self - other as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(4.0)
		    >>> y = x - Dual(2.0, der=2.0)
		    >>> print(y.val, y.der)
		    2.0 -1.0

		"""

		return self + (-1) * other

	def __rsub__(self, other):
		"""Returns other - self as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, after '-'.
		    other: a Dual or a real number, before '-'.

		    RETURNS
		    ========
		    other - self as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(4.0)
		    >>> y = 1.0 - x
		    >>> print(y.val, y.der)
		    -3.0 -1.0

		"""

		return other + (-1)*self

	def __mul__(self, other):
		"""Returns self * other as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, before '*'.
		    other: a Dual or a real number, after '*'.

		    RETURNS
		    ========
		    self * other as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(4.0)
		    >>> y = x * Dual(2.0, der=2.0)
		    >>> print(y.val, y.der)
		    8.0 2.0

		"""

		try:
			val = self.val * other.val
			der = self.der * other.val + self.val * other.der
		except AttributeError:
			val = self.val * other
			der = self.der * other
		return Dual(val, der)

	def __rmul__(self, other):
		"""Returns other * self as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, after '*'.
		    other: a Dual or a real number, before '*'.

		    RETURNS
		    ========
		    other * self as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(4.0)
		    >>> y = 1.0 * x
		    >>> print(y.val, y.der)
		    4.0 1.0

		"""

		return self * other

	def __truediv__(self, other):
		"""Returns self / other as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, before '/'.
		    other: a Dual or a real number, after '/'.

		    RETURNS
		    ========
		    self / other as a Dual.

		    EXAMPLES
		    =========
			>>> x = Dual(9.0)
			>>> y = x / 2
			>>> print(y.val, y.der)
			4.5 0.5

		"""

		return self * (other ** (-1))

	def __rtruediv__(self, other):
		"""Returns other / self as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, after '/'.
		    other: a Dual or a real number, before '/'.

		    RETURNS
		    ========
		    other / self as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(4.0)
			>>> y = 3.0 / x
			>>> print(y.val, y.der)
			0.75 - 0.1875

		"""

		return other * (self ** (-1))

	def __pow__(self,other):
		"""Returns self ** other as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, before '**'.
		    other: a Dual or a real number, after '**'.

		    RETURNS
		    ========
		    self ** other as a Dual.

		    EXAMPLES
		    =========
		    >>> x = Dual(1.0)
			>>> y = 2
			>>> z = x**y
			>>> print(z.val,z.der)
		    1.0 2.0

		"""

		try:
			val = self.val ** other.val
			der = other.val * self.val ** (other.val - 1) * self.der + val * other.der * np.log(self.val)
		except AttributeError:
			val = self.val ** other
			der = other * (self.val ** (other-1)) * self.der
		return Dual(val, der)

	def __rpow__(self,other):
		"""Returns other ** self as a Dual.

		    INPUTS
		    =======
		    self: recent Dual, after '**'.
		    other: a Dual or a real number, before '**'.

		    RETURNS
		    ========
		    other ** self as a Dual.

		    EXAMPLES
		    =========
		   >>> x = Dual(3.0)
			>>> y = 2
			>>> z = y**x
			>>> print(z.val,z.der)
		    8.0 5.545177444479562

		"""

		val = other ** self.val
		der = val * np.log(other) * self.der
		return Dual(val, der)

	def diff(self, function):
		return function(self)


class AD():

	def __init__(self):
		pass

	def diff(self, function, dual):
		'''
		INPUTS
		=======
		function:  scalar function with more than one parameters: f(x1, x2)
		dual: a vector Dual (Dual of array: dual = LaplaceDiff.Dual(np.array([3.0,2.0,7.0])) ),
			  each element must have same length of val and der
		RETURNS
		========
		val: float, the value of the function
		der: the differential value of the function w.r.t. to the parameters
		EXAMPLES
		=========
		>>>def f(li):
		>>>return li[0] ** li[1] + li[2] ** 2
		>>>dual = LaplaceDiff.Dual(np.array([3.0,2.0,7.0]))
		>>>ad = LaplaceDiff.AD()
		>>>dual_f = ad.diff(f, dual)
		>>>print(dual_f.val)
		>>>print(dual_f.der)
		>>>58.0
		>>>[ 6.         9.8875106 14.       ]
		'''

		
		try:
			n = len(dual.val)
			der = []
			for i in range(n):
				li = []
				for j in dual.val:
					li.append(j)
				li[i] = Dual(dual.val[i], dual.der[i])
				if len(li) == 1:
					g = function(*li)
				else:
					g = function(li)
				try:
					val = g.val
					der.append(g.der)
				except AttributeError:
					# val = g
					# der.append('null')
					raise AttributeError("Function input dimension and dual dimension don't match")
		except TypeError:
			g = function(dual)
			val = g.val
			der = g.der
			# try:
			# 	val = g.val
			# 	der = g.der
			# except AttributeError:
			# 	val = g
			# 	der.append('null')
		# print(val, der)
		return Dual(val, np.array(der))

	def jacobian(self, vec_function, dual):
		'''
		INPUTS
		=======
		vec_function:  an array of scalar functions with more than one parameters: np.array([f_1(x1, x2),f_2(x_1,x_2,x_3))]
		dual: a Dual of array ( dual = LaplaceDiff.Dual(np.array([[3.0,2.0,7.0],[2.0,1.0,7.0]])) ),
		each element must have same length of val and der
		RETURNS
		========
		val: np.array, each element stands for the value of each function
		der: np.array, Each rows stands for the differential of each function.
		     Each element represents the differential value of the function over this variable.
		EXAMPLES
		=========
		>>>def f_1(li):
		>>>return li[0] ** li[1]
		>>>def f_2(li):
		>>>return li[2] ** (li[1] ** 2)
		>>>f = np.array([f_1,f_2])
		>>>dual = LaplaceDiff.Dual(np.array([3.0,2.0,7.0]))
		>>>ad = LaplaceDiff.AD()
		>>>val, der = ad.jacobian(f,dual)
		>>>print(val)
		>>>print(der)
		>>>[   9. 2401.]
		>>>[['6.0' '9.887510598012987' 'null']
        >>> ['null' '18688.52107152723' '1372.0']]
        '''

		der_li = []
		val_li = []
		for function in vec_function:
			dual_f = self.diff(function, dual)
			val_li.append(dual_f.val)
			der_li.append(dual_f.der)
		return np.array(val_li), np.array(der_li)

