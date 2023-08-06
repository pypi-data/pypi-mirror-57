import pytest
from LaplaceDiff.LaplaceDiff import Dual, AD
import numpy as np

def test_init():
	x = Dual([2,2])
	assert len(x.der) == 2
	x = Dual([2,2],[1,2])
	assert (x.der == np.array([1,2])).all()
	x = Dual(np.array([2,2]),np.array([1,2]))
	assert (x.der == np.array([1,2])).all()
	try:
		x = Dual(np.array([2,2]),np.array([1,2,3]))
	except ValueError:
		assert True
	try:
		x = Dual(np.array([2,2]),3)
	except ValueError:
		assert True

def test_pos():
	x = Dual(-4.0)
	y = + x
	assert np.isclose(y.val,-4.0)
	assert np.isclose(y.der,1.0)

def test_neg():
	x = Dual(-4.0)
	y = - x
	assert np.isclose(y.val,4.0)
	assert np.isclose(y.der,-1.0)
	
def test_eq():
	x = Dual(-4.0, 3.0)
	y = Dual(-4.0, 2.0)
	z = Dual(-4.0, 2.0)
	assert (y == z) == True
	assert (x == z) == False
	assert (x == 1.0) == False  # maybe raise and catch type error instead - modify later
	assert (Dual([1,2])==Dual([1,2])) == True
	assert (Dual([1,2],[1,1])==Dual([1,2],[1,2])) == False
	
def test_ne():
	x = Dual(-4.0, 3.0)
	y = Dual(-4.0, 2.0)
	z = Dual(-4.0, 2.0)
	assert (y != x) == True
	assert (y != z) == False
	assert (y != 1.0) == True
	assert (Dual([1,2])!=Dual([3,2])) == True

def test_add():
	x = Dual(4.0)
	y = x + 1.0
	z = x + Dual(3.0, 2.0)
	assert np.isclose(y.val, 5.0)
	assert np.isclose(y.der, 1.0)
	assert np.isclose(z.val, 7.0)
	assert np.isclose(z.der, 3.0)

def test_radd():
	x = Dual(4.0)
	y = 1.0 + x
	assert np.isclose(y.val, 5.0)
	assert np.isclose(y.der, 1.0)

def test_sub():
	x = Dual(4.0)
	y = x - 1.0
	assert np.isclose(y.val, 3.0)
	assert np.isclose(y.der, 1.0)
	
def test_rsub():
	x = Dual(4.0)
	y = 1.0 - x
	assert np.isclose(y.val, -3.0)
	assert np.isclose(y.der, -1.0)

def test_mul():
	x = Dual(4.0)
	y = x * 2.0
	z = x * Dual(2.0, 2.0)
	assert np.isclose(y.val, 8.0)
	assert np.isclose(y.der, 2.0)
	assert np.isclose(z.val, 8.0)
	assert np.isclose(z.der, 10.0)
	
def test_rmul():
	x = Dual(4.0)
	y = 3.0 * x
	assert np.isclose(y.val, 12.0)
	assert np.isclose(y.der, 3.0)

def test_truediv():
	x = Dual(4.0)
	y = x / 2.0
	assert np.isclose(y.val, 2.0)
	assert np.isclose(y.der, 0.5)
	
def test_rtruediv():
	x = Dual(4.0)
	y = 1.0 / x
	assert np.isclose(y.val, 0.25)
	assert np.isclose(y.der, -0.0625)

def test_pow():
	x = Dual(1.0)
	y = x ** 2
	z = x ** Dual(3, 2)
	assert np.isclose(y.val, 1.0)
	assert np.isclose(y.der, 2.0)
	assert np.isclose(z.val, 1.0)
	assert np.isclose(z.der, 3.0)
	
def test_rpow():
	x = Dual(1.0)
	y = 2 ** x
	assert np.isclose(y.val, 2.0)
	assert np.isclose(y.der, 1.3862943611198906)

def test_AD():
	ad = AD()
	function = lambda x: 2*x + 1
	x = Dual(1.0)
	assert ad.diff(function, x) == Dual(3.0,2.0)

def test_diff():
	ad = AD()
	function = lambda x: 2*x + 1
	x = Dual(1.0)
	dual_f = ad.diff(function, x)
	assert np.isclose(dual_f.val, 3.)
	assert (dual_f.der == np.array([2.])).all()

def test_jacobian():
	ad = AD()
	function = lambda x: 2 * x + 1
	f = np.array([function])
	x = Dual(np.array([1.0]))
	val, der = ad.jacobian(f, x)
	assert (val == np.array([3.])).all()
	assert (der == np.array([[2.]])).all()
