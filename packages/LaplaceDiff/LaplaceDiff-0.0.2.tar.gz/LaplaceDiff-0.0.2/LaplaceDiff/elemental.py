import numpy as np
from LaplaceDiff.LaplaceDiff import Dual

def exp(x):
	"""Returns exponential of a Dual.
    
    INPUTS
    =======
    x: a Dual or real number
    
    RETURNS
    ========
    exponential of x
    
    EXAMPLES
    =========
    >>> x = Dual(0)
    >>> y = exp(x)
    >>> print(y.val, y.der)
    1.0 1.0
    """
	try:
		val = np.exp(x.val)
		der = x.der * val
		return Dual(val, der)
	except AttributeError:
		return np.exp(x)

def log(x):
	"""Returns logarithm of a Dual.
    
    INPUTS
    =======
    x: a Dual or real number
    
    RETURNS
    ========
    logarithm of x
    
    EXAMPLES
    =========
    >>> x = Dual(1.0)
    >>> y = log(x)
    >>> print(y.val, y.der)
    0.0 1.0
    """
	try:
		val = np.log(x.val)
		der = x.der / x.val
		return Dual(val, der)
	except AttributeError:
		return np.log(x)

def sin(x):
	"""Returns sin of a Dual.
    
    INPUTS
    =======
    x: a Dual or real number, radian
    
    RETURNS
    ========
    sin of x
    
    EXAMPLES
    =========
    >>> x = Dual(1.0)
    >>> y = sin(x)
    >>> print(y.val, y.der)
    0.841470984808 0.540302305868
    """
	try:
		val = np.sin(x.val)
		der = np.cos(x.val) * x.der
		return Dual(val, der)
	except AttributeError:
		return np.sin(x)	

def cos(x):
	"""Returns sin of a Dual.
    
    INPUTS
    =======
    x: a Dual or real number, radian
    
    RETURNS
    ========
    sin of x
    
    EXAMPLES
    =========
    >>> x = Dual(1.0)
    >>> y = cos(x)
    >>> print(y.val, y.der)
    0.540302305868 -0.841470984808
    """
	try:
		val = np.cos(x.val)
		der = - np.sin(x.val) * x.der
		return Dual(val, der)
	except AttributeError:
		return np.cos(x)	

def tan(x):
	"""Returns sin of a Dual.
    
    INPUTS
    =======
    x: a Dual or real number, radian
    
    RETURNS
    ========
    sin of x
    
    EXAMPLES
    =========
    >>> x = Dual(1.0)
    >>> y = tan(x)
    >>> print(y.val, y.der)
    1.55740772465 3.42551882081
    """
	try:
		val = np.tan(x.val)
		der = x.der / (np.cos(x.val)**2)
		return Dual(val, der)
	except AttributeError:
		return np.tan(x)

# def main():
	# '''run some simple tests'''
	# x = Dual([0,0],[1,1])
	# y = exp(x)
	# print(y.val, y.der)
	# assert (y.val == np.exp(0)).all()

	# x = Dual(1.0)
	# y = log(x)
	# print(y.val, y.der)

	# x = Dual(1.0)
	# y = sin(x)
	# print(y.val, y.der)

	# x = Dual(1.0)
	# y = cos(x)
	# print(y.val, y.der)

	# x = Dual(1.0, 5.0)
	# y = tan(x)
	# assert y.val == np.tan(1.0)
	# assert y.der == 5.0 / (np.cos(1.0) **2)
	# print(y.der - 1.0/ (np.cos(1.0) **2) * 5)
    # pass



if __name__ == '__main__':
	# main()
    pass