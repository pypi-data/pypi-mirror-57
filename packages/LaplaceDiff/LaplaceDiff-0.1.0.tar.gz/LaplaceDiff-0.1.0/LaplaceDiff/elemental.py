import numpy as np
from LaplaceDiff.LaplaceDiff import Dual

def exp(x, base="e"):
    """Returns exponential of a Dual.
    
    INPUTS
    =======
    x: a Dual or real number
    base: "e" or a positive real number
    
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
    if base == "e":
        try:
            val = np.exp(x.val)
            der = x.der * val
            return Dual(val, der)
        except AttributeError:
            return np.exp(x)
    else:
        if base <= 0:
            raise ValueError("Base must be a positive real number.")
        try:
            val = np.power(base, x.val)
            der = x.der * np.log(base) * val
            return Dual(val, der)
        except AttributeError:
            return np.power(base, x.val)

def log(x, base="e"):
    """Returns logarithm of a Dual.
    
    INPUTS
    =======
    x: a Dual or real number
    base: "e" or a positive real number not equal one.
    
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
    if base == "e":
        try:
            val = np.log(x.val)
            der = x.der / x.val
            return Dual(val, der)
        except AttributeError:
            return np.log(x)
    else:
        if base <= 0 or base == 1:
            raise ValueError("Base must be a positive real number not equal one.")
        try:
            val = np.log(x.val) / np.log(base)
            der = x.der / (x.val * np.log(base))
            return Dual(val, der)
        except AttributeError:
            return np.log(x) / np.log(base)

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

def arcsin(x):
 	"""Returns arcsin of a Dual.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     arcsin of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = arcsin(x)
     >>> print(y.val, y.der)
     0.5235987755982989 1.1547005383792517
     """
 	try:
 		val = np.arcsin(x.val)
 		der = x.der / np.sqrt(1-np.power(x.val,2))
 		return Dual(val, der)
 	except AttributeError:
 		return np.arcsin(x)	

def arccos(x):
 	"""Returns arccos of a Dual.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     arccos of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = arccos(x)
     >>> print(y.val, y.der)
     1.0471975511965979 -1.1547005383792517
     """
 	try:
 		val = np.arccos(x.val)
 		der = -x.der / np.sqrt(1-np.power(x.val,2))
 		return Dual(val, der)
 	except AttributeError:
 		return np.arccos(x)	

def arctan(x):
 	"""Returns arctan of a Dual.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     arctan of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = arctan(x)
     >>> print(y.val, y.der)
     0.4636476090008061 0.8
     """
 	try:
 		val = np.arctan(x.val)
 		der = x.der / (1 + np.power(x.val,2))
 		return Dual(val, der)
 	except AttributeError:
 		return np.arctan(x)	

def sinh(x):
 	"""Returns sinh of a Dual.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     sinh of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = sinh(x)
     >>> print(y.val, y.der)
     0.5210953054937474 1.1276259652063807
     """
 	try:
 		val = np.sinh(x.val)
 		der = np.cosh(x.val) * x.der
 		return Dual(val, der)
 	except AttributeError:
 		return np.sinh(x)	

def cosh(x):
 	"""Returns cosh of a Dual.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     cosh of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = cosh(x)
     >>> print(y.val, y.der)
     1.1276259652063807 0.5210953054937474
     """
 	try:
 		val = np.cosh(x.val)
 		der = np.sinh(x.val) * x.der
 		return Dual(val, der)
 	except AttributeError:
 		return np.cosh(x)

def tanh(x):
 	"""Returns tanh of a Dual.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     tanh of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = tanh(x)
     >>> print(y.val, y.der)
     0.46211715726000974 0.7864477329659275
     """
 	try:
 		val = np.tanh(x.val)
 		der = x.der / np.power(np.cosh(x.val),2)
 		return Dual(val, der)
 	except AttributeError:
 		return np.tanh(x)

def sqrt(x):
 	"""Returns sqrt of a Dual.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     sqrt of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = sqrt(x)
     >>> print(y.val, y.der)
     0.7071067811865476 0.7071067811865475
     """
 	try:
 		val = np.sqrt(x.val)
 		der = x.der / (2 * np.sqrt(x.val))
 		return Dual(val, der)
 	except AttributeError:
 		return np.sqrt(x)

def logistic(x):
 	"""Returns logistic of a Dual. With standard logistic params.
     
     INPUTS
     =======
     x: a Dual or real number, radian
     
     RETURNS
     ========
     logistic of x
     
     EXAMPLES
     =========
     >>> x = Dual(0.5)
     >>> y = logistic(x)
     >>> print(y.val, y.der)
     0.6224593312018546 0.2350037122015945
     """
 	try:
 		val = np.exp(x.val)/(1+np.exp(x.val))
 		der = x.der * np.exp(-x.val) / np.power(1+np.exp(-x.val),2)
 		return Dual(val, der)
 	except AttributeError:
 		return np.log(x)


if __name__ == '__main__':
	# main()
    pass